# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_frm_login(object):
    def setupUi(self, frm_login):
        if not frm_login.objectName():
            frm_login.setObjectName(u"frm_login")
        frm_login.resize(466, 364)
        self.layoutWidget = QWidget(frm_login)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 80, 301, 161))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.txt_account = QLineEdit(self.layoutWidget)
        self.txt_account.setObjectName(u"txt_account")

        self.horizontalLayout.addWidget(self.txt_account)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.txt_pwd = QLineEdit(self.layoutWidget)
        self.txt_pwd.setObjectName(u"txt_pwd")

        self.horizontalLayout_2.addWidget(self.txt_pwd)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_login = QPushButton(self.layoutWidget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setFont(font1)

        self.horizontalLayout_3.addWidget(self.btn_login)

        self.btn_cancel = QPushButton(self.layoutWidget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFont(font1)

        self.horizontalLayout_3.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(frm_login)

        QMetaObject.connectSlotsByName(frm_login)
    # setupUi

    def retranslateUi(self, frm_login):
        frm_login.setWindowTitle(QCoreApplication.translate("frm_login", u"\u7528\u6237\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("frm_login", u"\u8d26\u53f7:", None))
        self.label_2.setText(QCoreApplication.translate("frm_login", u"\u5bc6\u7801:", None))
        self.btn_login.setText(QCoreApplication.translate("frm_login", u"\u767b\u5f55", None))
        self.btn_cancel.setText(QCoreApplication.translate("frm_login", u"\u53d6\u6d88", None))
    # retranslateUi

