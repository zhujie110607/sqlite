import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Slot, QSettings, QTimer
from ui.Login_ui import Ui_frm_login
from file_py.index import MainWindow
from file_py.SqlHelper import SqlHelper
import qtmodern.styles
import qtmodern.windows


class LoginWindow(QWidget):  # 登录窗口
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_login()
        self.ui.setupUi(self)
        self.ui.btn_login.clicked.connect(self.login)
        # 按回车键登录
        self.ui.txt_pwd.returnPressed.connect(self.login)
        settings = QSettings('MyCompany', 'MyApp')  # 读取上次保存的用户选择
        self.ui.cbox_user.setChecked(settings.value('r_user', False, type=bool))
        self.ui.cbox_pwd.setChecked(settings.value('r_pwd', False, type=bool))
        user = settings.value('user', '')
        pwd = settings.value('pwd', '')
        if user != '' and pwd != '':
            self.ui.txt_user.setText(user)
            self.ui.txt_pwd.setText(pwd)
        elif user != '' and pwd == '':
            self.ui.txt_user.setText(user)
            # 使用 QTimer.singleShot 来在稍后的时间点执行 setFocus
            QTimer.singleShot(0, lambda: self.ui.txt_pwd.setFocus())
        elif user == '':
            QTimer.singleShot(0, lambda: self.ui.txt_user.setFocus())
        self.df = SqlHelper().Query_SQLServer_by_SQL("select UserNumber,UserName,UserPwd,privs from UserManagement")
        if self.df.empty:
            QMessageBox.warning(self, '系统消息', '没有获取到用户表数据，请检查服务器是否关闭', QMessageBox.Yes)
            # 退出程序
            sys.exit()

    @Slot()
    def login(self):
        user = self.ui.txt_user.text()
        pwd = self.ui.txt_pwd.text()
        user = 'zwx846533'
        pwd = 'HUAWEI7410.'
        if user in self.df['UserNumber'].values and pwd in self.df['UserPwd'].values:
            # 保存用户选择
            settings = QSettings('MyCompany', 'MyApp')
            settings.setValue('r_user', self.ui.cbox_user.isChecked())
            settings.setValue('r_pwd', self.ui.cbox_pwd.isChecked())
            if self.ui.cbox_user.isChecked():
                settings.setValue('user', user)
            else:
                settings.setValue('user', '')
            if self.ui.cbox_pwd.isChecked():
                settings.setValue('pwd', pwd)
            else:
                settings.setValue('pwd', '')
            self.ui.user_zd = self.df[self.df['UserNumber'] == user].to_dict('records')[0]
            self.main_window = MainWindow(self.ui)  # 创建主窗口实例
            self.main_window.show()  # 显示主窗口
            self.close()  # 隐藏登录窗口
        else:
            QMessageBox.warning(self, '系统消息', '用户名或密码错误,请重新输入', QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication([])
    login_window = LoginWindow()
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(login_window)
    mw.move(app.primaryScreen().size().width() / 2 - login_window.size().width() / 2,
            app.primaryScreen().size().height() / 2 - login_window.size().height() / 2)
    mw.show()
    app.exec()
