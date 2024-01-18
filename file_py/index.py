import sys
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
from ui.main_ui import Ui_MainWindow
from file_py.file_operations import FileManager
from file_py.user import Useradmin
from file_py.update_user import UpdateUser
from file_py.common import Variable
import pandas as pd


class MainWindow(QMainWindow):  # 主窗口
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fileManager = FileManager()
        if Variable.user_zd['privs'] == 0:  # 设置非管理员权限
            self.ui.action_add.setVisible(False)
            self.ui.action_update.setVisible(False)
            self.ui.action_delete.setVisible(False)
            self.ui.user_adm.setVisible(False)
        self.setupTableStructure()  # 绑定表格
        self.bind()

    def setupTableStructure(self):
        # 设置表格自适应内容宽度
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置行文字大小
        font = QFont()
        font.setPointSize(12)
        self.ui.table.setFont(font)

    def bind(self):
        self.ui.action_add.triggered.connect(self.fileManager.add)  # 添加
        self.ui.action_update.triggered.connect(self.fileManager.update)  # 修改
        self.ui.action_delete.triggered.connect(self.fileManager.delete)  # 删除
        self.ui.action_query.triggered.connect(self.fileManager.export)  # 查询
        self.ui.action_match.triggered.connect(self.fileManager.match)  # 匹配
        self.ui.txtScan.returnPressed.connect(self.on_return_pressed)  # 回车键查询
        self.ui.user_adm.triggered.connect(self.userFrom)
        self.ui.pwd_update.triggered.connect(self.update_userFrom)

    def userFrom(self):
        self.ui.useradmin = Useradmin()
        self.ui.useradmin.show()

    def update_userFrom(self):
        self.ui.updateUser = UpdateUser()
        self.ui.updateUser.show()

    def on_return_pressed(self):
        try:
            user_input = self.ui.txtScan.text().strip()  # 获取用户输入的内容
            item = ''
            date = ''
            flig = True  # 如果用户输入的是条码（长度为16或20），则为True，如果是编码（长度小于16大于0）否则为False
            # 判断用户输入的内容去除前后空格后是否为空
            if user_input:
                # 如果user_input的长度等于16，则提取前6位，如果长度等于20位，则提取第3位至第10位
                if len(user_input) == 16:
                    item = '03' + user_input[:6]
                elif len(user_input) == 20:
                    item = user_input[2:10]
                elif len(user_input) < 16 and len(user_input) > 0:
                    item = user_input
                    flig = False
                else:
                    # 删除表格所有行
                    self.clearTable()
                    QMessageBox.warning(self, '警告', '长度不符合规范(长度范围：1-20)！')
                    return
            else:
                # 删除表格所有行
                self.clearTable()
                QMessageBox.warning(self, '警告', '长度不能为空！')
                return
            if flig:
                year = user_input[-8:-6]  # 截取出生产日期代号
                date = Variable.prodDate_df[Variable.prodDate_df['year'] == year]['date'].values[0]
                if date == None:
                    # 删除表格所有行
                    self.clearTable()
                    QMessageBox.warning(self, '警告', '生产日期不存在！')
                    return
            df = self.fileManager.query(str(item))
            if df.shape[0] == 0:
                # 删除表格所有行
                self.clearTable()
                QMessageBox.warning(self, '警告', '编码不存在！')
                return
            # self.ui.table.setRowCount(0)
            df.insert(0, 'SN', user_input)
            df.insert(2, 'date', date)
            self.load_data_to_table(df)
        except Exception as e:
            # 删除表格所有行
            self.clearTable()
            QMessageBox.warning(self, '警告', '查询失败！' + str(e))
        finally:
            self.ui.txtScan.clear()
            # 获取焦点
            self.ui.txtScan.setFocus()

    def load_data_to_table(self, df):
        # 删除表格所有行
        self.clearTable()
        r = 0
        for row in range(df.shape[0]):
            # 把df.iloc[row,4]按'//'分割成列表
            list = df.iloc[row, 4].split('/')
            c = 0
            for li in list:
                self.ui.table.insertRow(r)
                # 设置行高20
                self.ui.table.setRowHeight(r, 20)
                if c == 0:
                    self.ui.table.setItem(r, 0, QTableWidgetItem(str(df.iloc[row, 0])))
                    self.ui.table.setItem(r, 1, QTableWidgetItem(str(df.iloc[row, 1])))
                    self.ui.table.setItem(r, 2, QTableWidgetItem(str(df.iloc[row, 2])))
                    self.ui.table.setItem(r, 3, QTableWidgetItem(str(df.iloc[row, 3])))
                self.ui.table.setItem(r, 4, QTableWidgetItem(str(li)))
                c += 1
                r += 1

    def clearTable(self):
        # 删除表格所有行
        self.ui.table.setRowCount(0)
