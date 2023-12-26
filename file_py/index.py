import sys
from PySide6.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
from ui.main_ui import Ui_MainWindow
from file_py.file_operations import FileManager
import pandas as pd
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):  # 主窗口
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.user_zd = self.parent.user_zd  # 绑定用户数据
        self.fileManager = FileManager()
        if self.ui.user_zd['privs'] == 0:
            self.ui.menu.setEnabled(False)
        self.ui.tab_data.setHorizontalHeaderLabels(['条码', '编码', '生产日期', '当前版本', '历史版本'])
        self.ui.tab_data.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # 设置表头边框和字体加粗
        header_font = QFont()
        header_font.setBold(True)
        for col in range(self.ui.tab_data.columnCount()):
            header_item = QTableWidgetItem(self.ui.tab_data.horizontalHeaderItem(col))
            header_item.setFont(header_font)
            # header_item.setFlags(int(header_item.flags()) ^ 0x8000)  # 取消最后一行的边框
            self.ui.tab_data.setHorizontalHeaderItem(col, header_item)

        # 设置表格内容居中显示
        self.ui.tab_data.setStyleSheet(
            "QTableWidget QTableCornerButton::section{background: lightgray; border: 1px solid gray;}"
            "QTableWidget::item{border: 1px solid gray;}"
            "QHeaderView::section{background: lightgray; border: 1px solid gray;}"
            "QTableWidget QTableWidgetCornerButton::section{background: lightgray; border: 1px solid gray;}")

        try:
            self.ui.df = pd.read_excel('D:\\生产日期.xlsx', sheet_name='Sheet1', usecols=['年份', '生产日期'])
        except:
            QMessageBox.warning(self, '警告', '没有获取到D盘中生产日期表格数据')
            sys.exit()

        self.ui.df.rename(columns={'年份': 'year', '生产日期': 'date'}, inplace=True)
        self.bind()

    def bind(self):
        self.ui.action_add.triggered.connect(self.fileManager.add)  # 添加
        self.ui.action_update.triggered.connect(self.fileManager.update)  # 修改
        self.ui.action_delete.triggered.connect(self.fileManager.delete)  # 删除
        self.ui.action_query.triggered.connect(self.fileManager.query)  # 查询
        self.ui.txtScan.returnPressed.connect(self.on_return_pressed)  # 回车键查询

    def on_return_pressed(self):
        user_input = self.ui.txtScan.text()  # 获取用户输入的内容
        item = ''
        # 判断用户输入的内容去除前后空格后是否为空
        if user_input.strip():
            # 如果user_input的长度等于16，则提取前6位，如果长度等于20位，则提取第3位至第10位
            if len(user_input) == 16:
                item = '03' + user_input[:6]
            elif len(user_input) == 20:
                item = user_input[2:10]
            else:
                QMessageBox.warning(self, '警告', '条码长度不符合规范！')
                return
        year = user_input[-8:-6]  # 截取出生产日期代号
        date = self.ui.df[self.ui.df['year'] == year]['date'].values[0]
        if date == None:
            QMessageBox.warning(self, '警告', '生产日期不存在！')
            return
        df = self.fileManager.query(str(item))
        if df.shape[0] == 0:
            QMessageBox.warning(self, '警告', '编码不存在！')
            return
        # self.ui.tab_data.setRowCount(0)
        df.insert(0, 'SN', user_input)
        df.insert(2, 'date', date)
        self.load_data_to_table(df)

    def load_data_to_table(self, df):
        self.ui.tab_data.setRowCount(df.shape[0])
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[row, col]))
                self.ui.tab_data.setItem(row, col, item)
