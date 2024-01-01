import pandas as pd
from PySide6.QtWidgets import QWidget, QMessageBox
from ui.update_user_ui import Ui_Form
from file_py.common import Variable
from file_py.SqlHelper import SqlHelper


class UpdateUser(QWidget):
    def __init__(self):
        super(UpdateUser, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.txt_user.setText(Variable.user_zd['UserNumber'])
        self.sqlHelper = SqlHelper()
        self.bind()

    def bind(self):
        self.ui.btn_update.clicked.connect(self.updatePwd_user)

    def updatePwd_user(self):
        pwd = self.ui.txt_pwd.text()  # 获取新密码
        pwd2 = self.ui.txt_pwd2.text()  # 获取第二次输入的新密码
        # 判断新密码长度是否在6-16之间
        if len(pwd) < 6 or len(pwd) > 16:
            self.ui.txt_pwd.setText('')
            self.ui.txt_pwd2.setText('')
            self.ui.txt_pwd.setFocus()
            QMessageBox.warning(self, '警告', '密码长度在6-16之间！')
            return
        # 判断密码是否包含字母+数字
        if not any(i.isdigit() for i in pwd) or not any(i.isalpha() for i in pwd):
            self.ui.txt_pwd.setText('')
            self.ui.txt_pwd2.setText('')
            self.ui.txt_pwd.setFocus()
            QMessageBox.warning(self, '警告', '密码中必须包含字母和数字！')
            return
        # 判断新密码是否和原密码相同
        if pwd == Variable.user_zd['UserPwd']:
            self.ui.txt_pwd.setText('')
            self.ui.txt_pwd2.setText('')
            self.ui.txt_pwd.setFocus()
            QMessageBox.warning(self, '警告', '新密码不能与原密码相同！')
            return
        # 判断两次输入的新密码是否一致
        if pwd != pwd2:
            self.ui.txt_pwd.setText('')
            self.ui.txt_pwd2.setText('')
            self.ui.txt_pwd.setFocus()
            QMessageBox.warning(self, '警告', '两次输入的新密码不一致！')
            return
        if QMessageBox.warning(self, '警告', '确定修改密码？', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            if self.sqlHelper.update_userpwd(
                    pd.DataFrame([[Variable.user_zd['UserNumber'], pwd]], columns=['UserNumber', 'UserPwd'])) > 0:
                self.ui.txt_pwd.setText('')
                self.ui.txt_pwd2.setText('')
                self.ui.txt_pwd.setFocus()
                QMessageBox.information(self, '提示', '修改成功！')
            else:
                QMessageBox.warning(self, '警告', '修改失败！')
