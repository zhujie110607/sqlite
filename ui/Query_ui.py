# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Query.ui'
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
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.resize(544, 378)
        self.layoutWidget = QWidget(frm_main)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 50, 522, 297))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txtScan = QLineEdit(self.layoutWidget)
        self.txtScan.setObjectName(u"txtScan")

        self.horizontalLayout.addWidget(self.txtScan)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lab_barcode = QLabel(self.layoutWidget)
        self.lab_barcode.setObjectName(u"lab_barcode")

        self.horizontalLayout_2.addWidget(self.lab_barcode)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.lab_coding = QLabel(self.layoutWidget)
        self.lab_coding.setObjectName(u"lab_coding")

        self.horizontalLayout_3.addWidget(self.lab_coding)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.lab_makedate = QLabel(self.layoutWidget)
        self.lab_makedate.setObjectName(u"lab_makedate")

        self.horizontalLayout_4.addWidget(self.lab_makedate)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.C_version = QTextEdit(self.layoutWidget)
        self.C_version.setObjectName(u"C_version")

        self.horizontalLayout_5.addWidget(self.C_version)

        self.H_version = QTextEdit(self.layoutWidget)
        self.H_version.setObjectName(u"H_version")

        self.horizontalLayout_5.addWidget(self.H_version)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(frm_main)

        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"\u626b\u63cf\u67e5\u8be2", None))
        self.label.setText(QCoreApplication.translate("frm_main", u"\u626b\u63cf", None))
        self.label_2.setText(QCoreApplication.translate("frm_main", u"\u6761\u7801", None))
        self.lab_barcode.setText(QCoreApplication.translate("frm_main", u"\u6761\u7801", None))
        self.label_5.setText(QCoreApplication.translate("frm_main", u"\u7f16\u7801", None))
        self.lab_coding.setText(QCoreApplication.translate("frm_main", u"\u7f16\u7801", None))
        self.label_6.setText(QCoreApplication.translate("frm_main", u"\u751f\u4ea7\u65e5\u671f", None))
        self.lab_makedate.setText(QCoreApplication.translate("frm_main", u"\u751f\u4ea7\u65e5\u671f", None))
    # retranslateUi

