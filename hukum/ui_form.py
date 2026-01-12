# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.actionData_Pemilik = QAction(main)
        self.actionData_Pemilik.setObjectName(u"actionData_Pemilik")
        self.actionData_CV = QAction(main)
        self.actionData_CV.setObjectName(u"actionData_CV")
        self.actionData_CV_2 = QAction(main)
        self.actionData_CV_2.setObjectName(u"actionData_CV_2")
        self.actionData_Register = QAction(main)
        self.actionData_Register.setObjectName(u"actionData_Register")
        self.actionData_Register_CV = QAction(main)
        self.actionData_Register_CV.setObjectName(u"actionData_Register_CV")
        self.actionMenu_Laporan = QAction(main)
        self.actionMenu_Laporan.setObjectName(u"actionMenu_Laporan")
        self.actionData_Notaris = QAction(main)
        self.actionData_Notaris.setObjectName(u"actionData_Notaris")
        self.actionData_Petugas = QAction(main)
        self.actionData_Petugas.setObjectName(u"actionData_Petugas")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionData_Pemilik)
        self.menuMenu.addAction(self.actionData_CV_2)
        self.menuMenu.addAction(self.actionData_Register)
        self.menuMenu.addAction(self.actionData_Register_CV)
        self.menuMenu.addAction(self.actionMenu_Laporan)
        self.menuMenu.addAction(self.actionData_Notaris)
        self.menuMenu.addAction(self.actionData_Petugas)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionData_Pemilik.setText(QCoreApplication.translate("main", u"Data Pemilik", None))
        self.actionData_CV.setText(QCoreApplication.translate("main", u"Data Notaris", None))
        self.actionData_CV_2.setText(QCoreApplication.translate("main", u"Data CV", None))
        self.actionData_Register.setText(QCoreApplication.translate("main", u"Data Register", None))
        self.actionData_Register_CV.setText(QCoreApplication.translate("main", u"Data Register CV", None))
        self.actionMenu_Laporan.setText(QCoreApplication.translate("main", u"Menu Laporan", None))
        self.actionData_Notaris.setText(QCoreApplication.translate("main", u"Data Notaris", None))
        self.actionData_Petugas.setText(QCoreApplication.translate("main", u"Data Petugas", None))
        self.menuMenu.setTitle(QCoreApplication.translate("main", u"Menu", None))
    # retranslateUi

