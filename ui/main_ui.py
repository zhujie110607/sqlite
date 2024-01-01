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
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1170, 500)
        MainWindow.setMinimumSize(QSize(1170, 300))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setSizeIncrement(QSize(0, 0))
        self.action_add = QAction(MainWindow)
        self.action_add.setObjectName(u"action_add")
        self.action_update = QAction(MainWindow)
        self.action_update.setObjectName(u"action_update")
        self.action_delete = QAction(MainWindow)
        self.action_delete.setObjectName(u"action_delete")
        self.action_query = QAction(MainWindow)
        self.action_query.setObjectName(u"action_query")
        self.action_match = QAction(MainWindow)
        self.action_match.setObjectName(u"action_match")
        self.user_adm = QAction(MainWindow)
        self.user_adm.setObjectName(u"user_adm")
        self.pwd_update = QAction(MainWindow)
        self.pwd_update.setObjectName(u"pwd_update")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1170, 0))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txtScan = QLineEdit(self.centralwidget)
        self.txtScan.setObjectName(u"txtScan")
        self.txtScan.setMinimumSize(QSize(1100, 0))
        palette = QPalette()
        brush = QBrush(QColor(29, 233, 182, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(29, 233, 182, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.txtScan.setPalette(palette)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.txtScan.setFont(font)

        self.verticalLayout.addWidget(self.txtScan)

        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 5):
            self.table.setColumnCount(5)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table.setObjectName(u"table")
        self.table.setMinimumSize(QSize(1170, 0))
        self.table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1170, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_add)
        self.menu.addAction(self.action_update)
        self.menu.addSeparator()
        self.menu.addAction(self.action_match)
        self.menu.addAction(self.action_query)
        self.menu.addSeparator()
        self.menu.addAction(self.action_delete)
        self.menu_2.addAction(self.user_adm)
        self.menu_2.addAction(self.pwd_update)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u7248\u672c\u7ba1\u7406", None))
        self.action_add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.action_update.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.action_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.action_query.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.action_match.setText(QCoreApplication.translate("MainWindow", u"\u5339\u914d", None))
        self.user_adm.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u7528\u6237", None))
        self.pwd_update.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5bc6\u7801", None))
#if QT_CONFIG(tooltip)
        self.txtScan.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.txtScan.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.txtScan.setText("")
        self.txtScan.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u626b\u63cf\u6761\u7801", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u6761\u7801", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u751f\u4ea7\u65e5\u671f", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7248\u672c", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5386\u53f2\u7248\u672c", None));
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u7ba1\u7406", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u7ba1\u7406", None))
    # retranslateUi

