# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_user.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(570, 320)
        Form.setMinimumSize(QSize(570, 320))
        Form.setMaximumSize(QSize(570, 320))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.txt_user = QLineEdit(Form)
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
        self.txt_user.setReadOnly(True)

        self.horizontalLayout.addWidget(self.txt_user)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.txt_pwd = QLineEdit(Form)
        self.txt_pwd.setObjectName(u"txt_pwd")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        self.txt_pwd.setPalette(palette1)
        self.txt_pwd.setFont(font1)
        self.txt_pwd.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.txt_pwd)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.txt_pwd2 = QLineEdit(Form)
        self.txt_pwd2.setObjectName(u"txt_pwd2")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        self.txt_pwd2.setPalette(palette2)
        self.txt_pwd2.setFont(font1)
        self.txt_pwd2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.txt_pwd2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btn_update = QPushButton(Form)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setFont(font)

        self.verticalLayout.addWidget(self.btn_update)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4fee\u6539\u5bc6\u7801", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7:", None))
        self.txt_user.setInputMask("")
        self.txt_user.setText("")
        self.txt_user.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u65b0\u5bc6\u7801:", None))
        self.txt_pwd.setInputMask("")
        self.txt_pwd.setText("")
        self.txt_pwd.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u65b0\u5bc6\u7801", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8bf7\u518d\u6b21\u8f93\u5165\u65b0\u5bc6\u7801:", None))
        self.txt_pwd2.setText("")
        self.txt_pwd2.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u518d\u6b21\u8f93\u5165\u65b0\u5bc6\u7801", None))
        self.btn_update.setText(QCoreApplication.translate("Form", u"\u4fee\u6539", None))
    # retranslateUi

