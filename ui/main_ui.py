# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1710, 858)
        self.action_add = QAction(MainWindow)
        self.action_add.setObjectName(u"action_add")
        self.action_update = QAction(MainWindow)
        self.action_update.setObjectName(u"action_update")
        self.action_delete = QAction(MainWindow)
        self.action_delete.setObjectName(u"action_delete")
        self.action_query = QAction(MainWindow)
        self.action_query.setObjectName(u"action_query")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txtScan = QLineEdit(self.centralwidget)
        self.txtScan.setObjectName(u"txtScan")
        self.txtScan.setGeometry(QRect(500, 10, 291, 31))
        self.tab_data = QTableWidget(self.centralwidget)
        if (self.tab_data.columnCount() < 5):
            self.tab_data.setColumnCount(5)
        self.tab_data.setObjectName(u"tab_data")
        self.tab_data.setGeometry(QRect(10, 60, 1681, 771))
        self.tab_data.setColumnCount(5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1710, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_add)
        self.menu.addAction(self.action_update)
        self.menu.addAction(self.action_query)
        self.menu.addAction(self.action_delete)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u7248\u672c\u7ba1\u7406", None))
        self.action_add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.action_update.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.action_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.action_query.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
#if QT_CONFIG(tooltip)
        self.txtScan.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txtScan.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.txtScan.setText("")
        self.txtScan.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u626b\u63cf\u6761\u7801", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u7ba1\u7406", None))
    # retranslateUi

