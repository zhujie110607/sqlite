# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(325, 200)
        Form.setMinimumSize(QSize(325, 200))
        Form.setMaximumSize(QSize(325, 200))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 57, 25))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.line_user = QLineEdit(self.frame)
        self.line_user.setObjectName(u"line_user")
        self.line_user.setGeometry(QRect(90, 10, 201, 30))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        self.line_user.setFont(font1)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 90, 51, 30))
        self.label_2.setFont(font)
        self.line_pwd = QLineEdit(self.frame)
        self.line_pwd.setObjectName(u"line_pwd")
        self.line_pwd.setGeometry(QRect(90, 90, 201, 30))
        self.line_pwd.setFont(font1)
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(200, 140, 79, 20))
        self.checkBox.setFont(font)
        self.btn_submit = QPushButton(self.frame)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setGeometry(QRect(90, 130, 75, 31))
        self.btn_submit.setFont(font)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 50, 57, 25))
        self.label_3.setFont(font)
        self.line_name = QLineEdit(self.frame)
        self.line_name.setObjectName(u"line_name")
        self.line_name.setGeometry(QRect(90, 50, 201, 30))
        self.line_name.setFont(font1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u7528\u6237", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\uff1a", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u7ba1\u7406\u5458", None))
        self.btn_submit.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u59d3\u540d\uff1a", None))
    # retranslateUi

