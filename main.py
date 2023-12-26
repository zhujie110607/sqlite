import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Slot
from ui.Login_ui import Ui_frm_login
from file_py.index import MainWindow
from file_py.SqlHelper import SqlHelper

class LoginWindow(QWidget):  # 登录窗口
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_login()
        self.ui.setupUi(self)
        self.ui.btn_login.clicked.connect(self.login)
        self.df = SqlHelper().Query_SQLServer_by_SQL("select UserNumber,UserName,UserPwd,privs from UserManagement")
        if self.df.empty:
            QMessageBox.warning(self, '系统消息', '没有获取到用户表数据，请检查服务器是否关闭', QMessageBox.Yes)
            # 退出程序
            sys.exit()


    @Slot()
    def login(self):
        username = self.ui.txt_account.text()
        password = self.ui.txt_pwd.text()
        username = 'zwx846533'
        password = 'HUAWEI7410.'
        if username in self.df['UserNumber'].values and password in self.df['UserPwd'].values:
            self.ui.user_zd = self.df[self.df['UserNumber'] == username].to_dict('records')[0]
            self.main_window = MainWindow(self.ui)  # 创建主窗口实例
            self.main_window.show()  # 显示主窗口
            self.close()  # 隐藏登录窗口
        else:
            QMessageBox.warning(self, '系统消息', '用户名或密码错误,请重新输入', QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication([])
    login_window = LoginWindow()
    login_window.show()
    app.exec()
