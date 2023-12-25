import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox,QMainWindow
from ui.Login_ui import Ui_frm_login
from ui.Query_ui import Ui_frm_main
from ui.main_ui import  Ui_MainWindow
from PySide6.QtCore import Slot
from SqlHelper import SqlHelper


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_login()
        self.ui.setupUi(self)
        self.ui.btn_login.clicked.connect(self.login)
        self.df = SqlHelper.Query_SQLServer("select UserNumber,UserName,UserPwd,privs from UserManagement")
        if self.df.empty:
            QMessageBox.warning(self, '系统消息', '没有获取到用户表数据，请检查服务器是否关闭', QMessageBox.Yes)
            # 退出程序
            sys.exit()

    @Slot()
    def login(self):
        username = self.ui.txt_account.text()
        password = self.ui.txt_pwd.text()
        username = 'wx876073'
        password = '123456'
        if username in self.df['UserNumber'].values and password in self.df['UserPwd'].values:
            self.ui.user_zd = self.df[self.df['UserNumber'] == username].to_dict('records')[0]
            self.main_window = MainWindow(self.ui)  # 创建主窗口实例
            self.main_window.show()  # 显示主窗口
            self.close()  # 隐藏登录窗口
        else:
            QMessageBox.warning(self, '系统消息', '用户名或密码错误,请重新输入', QMessageBox.Yes)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.user_zd = self.parent.user_zd



if __name__ == '__main__':
    app = QApplication([])
    login_window = LoginWindow()
    login_window.show()
    app.exec()
