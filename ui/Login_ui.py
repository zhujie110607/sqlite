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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_frm_login(object):
    def setupUi(self, frm_login):
        if not frm_login.objectName():
            frm_login.setObjectName(u"frm_login")
        frm_login.resize(357, 191)
        frm_login.setMinimumSize(QSize(357, 191))
        frm_login.setMaximumSize(QSize(357, 191))
        self.layoutWidget = QWidget(frm_login)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 341, 178))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.txt_user = QLineEdit(self.layoutWidget)
        self.txt_user.setObjectName(u"txt_user")
        palette = QPalette()
        brush = QBrush(QColor(29, 233, 182, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        self.txt_user.setPalette(palette)
        font1 = QFont()
        font1.setPointSize(20)
        self.txt_user.setFont(font1)

        self.horizontalLayout.addWidget(self.txt_user)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.txt_pwd = QLineEdit(self.layoutWidget)
        self.txt_pwd.setObjectName(u"txt_pwd")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        self.txt_pwd.setPalette(palette1)
        self.txt_pwd.setFont(font1)
        self.txt_pwd.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.txt_pwd)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.btn_login = QPushButton(self.layoutWidget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setFont(font)

        self.verticalLayout.addWidget(self.btn_login)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cbox_user = QCheckBox(self.layoutWidget)
        self.cbox_user.setObjectName(u"cbox_user")
        font2 = QFont()
        font2.setPointSize(14)
        self.cbox_user.setFont(font2)
        self.cbox_user.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.cbox_user.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.cbox_user)

        self.cbox_pwd = QCheckBox(self.layoutWidget)
        self.cbox_pwd.setObjectName(u"cbox_pwd")
        self.cbox_pwd.setFont(font2)
        self.cbox_pwd.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.cbox_pwd.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.cbox_pwd)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(frm_login)

        QMetaObject.connectSlotsByName(frm_login)
    # setupUi

    def retranslateUi(self, frm_login):
        frm_login.setWindowTitle(QCoreApplication.translate("frm_login", u"\u7528\u6237\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("frm_login", u"\u8d26\u53f7:", None))
        self.label_2.setText(QCoreApplication.translate("frm_login", u"\u5bc6\u7801:", None))
        self.txt_pwd.setText("")
        self.btn_login.setText(QCoreApplication.translate("frm_login", u"\u767b\u5f55", None))
        self.cbox_user.setText(QCoreApplication.translate("frm_login", u"\u8bb0\u4f4f\u7528\u6237\u540d", None))
        self.cbox_pwd.setText(QCoreApplication.translate("frm_login", u"\u8bb0\u4f4f\u5bc6\u7801", None))
    # retranslateUi

