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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(739, 590)
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
        self.H_version = QPlainTextEdit(self.centralwidget)
        self.H_version.setObjectName(u"H_version")
        self.H_version.setGeometry(QRect(350, 300, 331, 231))
        self.C_version = QPlainTextEdit(self.centralwidget)
        self.C_version.setObjectName(u"C_version")
        self.C_version.setGeometry(QRect(10, 300, 321, 231))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 80, 61, 181))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lab_coding = QLabel(self.layoutWidget)
        self.lab_coding.setObjectName(u"lab_coding")

        self.verticalLayout.addWidget(self.lab_coding)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(140, 80, 121, 181))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lab_sn = QLabel(self.layoutWidget_2)
        self.lab_sn.setObjectName(u"lab_sn")

        self.verticalLayout_2.addWidget(self.lab_sn)

        self.lab_item = QLabel(self.layoutWidget_2)
        self.lab_item.setObjectName(u"lab_item")

        self.verticalLayout_2.addWidget(self.lab_item)

        self.lab_makedate = QLabel(self.layoutWidget_2)
        self.lab_makedate.setObjectName(u"lab_makedate")

        self.verticalLayout_2.addWidget(self.lab_makedate)

        self.txtScan = QLineEdit(self.centralwidget)
        self.txtScan.setObjectName(u"txtScan")
        self.txtScan.setGeometry(QRect(70, 40, 401, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 739, 22))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6761\u7801", None))
        self.lab_coding.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u751f\u4ea7\u65e5\u671f", None))
        self.lab_sn.setText(QCoreApplication.translate("MainWindow", u"\u6761\u7801", None))
        self.lab_item.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801", None))
        self.lab_makedate.setText(QCoreApplication.translate("MainWindow", u"\u751f\u4ea7\u65e5\u671f", None))
        self.txtScan.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u7ba1\u7406", None))
    # retranslateUi

