from PySide6.QtWidgets import QWidget, QMessageBox
from ui.user_ui import Ui_Form
from file_py.SqlHelper import SqlHelper
from file_py.common import Variable
import pandas as pd


class Useradmin(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.sqlHelper = SqlHelper()
        self.bind()

    def bind(self):
        self.ui.btn_submit.clicked.connect(self.add_user)

    # 向数据库添加用户
    def add_user(self):
        user = self.ui.line_user.text()  # 获取账号
        name = self.ui.line_name.text()  # 获取姓名
        pwd = self.ui.line_pwd.text()  # 获取密码
        # 如果self.ui.checkBox被选中，则privs=1，否则privs=0
        privs = 0
        if self.ui.checkBox.isChecked():
            privs = 1

        if user == '' or name == '' or pwd == '':
            QMessageBox.warning(self, '警告', '账号、姓名、密码不能为空！')
            return
        # 判断账号在index.user_data中是否存在
        elif user in Variable.user_df['UserNumber'].values:
            QMessageBox.warning(self, '警告', '该账号已存在！')
            return
        # 判断账号长度是否在6-16之间
        elif len(user) < 6 or len(user) > 10:
            QMessageBox.warning(self, '警告', '账号长度不符合要求！')
            return
        # 判断密码长度是否在6-16之间
        elif len(pwd) < 6 or len(pwd) > 16:
            QMessageBox.warning(self, '警告', '密码长度不符合要求！')
            return
        # 判断密码是否包含字母+数字
        if not any(i.isdigit() for i in pwd) or not any(i.isalpha() for i in pwd):
            QMessageBox.warning(self, '警告', '密码中必须包含字母和数字！')
            return
        else:
            df = pd.DataFrame([[user, name, pwd, privs]], columns=['UserNumber', 'UserName', 'UserPwd', 'privs'])
            if self.sqlHelper.inster_user(df) > 0:
                Variable.user_df = pd.concat([Variable.user_df, df], ignore_index=True)
                QMessageBox.information(self, '提示', '添加成功！')
                self.ui.line_user.clear()
                self.ui.line_name.clear()
                self.ui.line_pwd.clear()
                self.ui.checkBox.setChecked(False)
            else:
                QMessageBox.warning(self, '警告', '添加失败！')
