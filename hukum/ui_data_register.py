# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_register.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1045, 568)
        self.frameHeader = QFrame(Form)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setGeometry(QRect(0, 0, 1050, 110))
        self.lblJudul1 = QLabel(self.frameHeader)
        self.lblJudul1.setObjectName(u"lblJudul1")
        self.lblJudul1.setGeometry(QRect(200, 10, 650, 25))
        self.lblJudul1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblJudul2 = QLabel(self.frameHeader)
        self.lblJudul2.setObjectName(u"lblJudul2")
        self.lblJudul2.setGeometry(QRect(200, 40, 650, 20))
        self.lblJudul2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblJudul3 = QLabel(self.frameHeader)
        self.lblJudul3.setObjectName(u"lblJudul3")
        self.lblJudul3.setGeometry(QRect(200, 65, 650, 20))
        self.lblJudul3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblCari = QLabel(Form)
        self.lblCari.setObjectName(u"lblCari")
        self.lblCari.setGeometry(QRect(20, 130, 300, 25))
        self.lblFilter = QLabel(Form)
        self.lblFilter.setObjectName(u"lblFilter")
        self.lblFilter.setGeometry(QRect(20, 165, 400, 20))
        self.cmbCari = QComboBox(Form)
        self.cmbCari.setObjectName(u"cmbCari")
        self.cmbCari.setGeometry(QRect(430, 160, 180, 30))
        self.btnCari = QPushButton(Form)
        self.btnCari.setObjectName(u"btnCari")
        self.btnCari.setGeometry(QRect(620, 160, 90, 30))
        self.tableRegister = QTableWidget(Form)
        self.tableRegister.setObjectName(u"tableRegister")
        self.tableRegister.setGeometry(QRect(20, 210, 1010, 300))
        self.btnKeluar = QPushButton(Form)
        self.btnKeluar.setObjectName(u"btnKeluar")
        self.btnKeluar.setGeometry(QRect(930, 520, 100, 30))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Pencarian Data Register CV", None))
        Form.setStyleSheet(QCoreApplication.translate("Form", u"\n"
"/* ================= GLOBAL ================= */\n"
"QWidget {\n"
"    background-color: #f2f2f2;\n"
"    font-family: Arial;\n"
"    font-size: 11px;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* ================= LABEL ================= */\n"
"QLabel {\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* ================= BUTTON ================= */\n"
"QPushButton {\n"
"    background-color: #e6e6e6;\n"
"    border: 1px solid #8a8a8a;\n"
"    border-radius: 4px;\n"
"    padding: 5px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #dcdcdc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #cfcfcf;\n"
"}\n"
"\n"
"/* ================= COMBOBOX ================= */\n"
"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #a0a0a0;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"/* ================= TABLE ================= */\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    gridline-color: #c0c0c0;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"   "
                        " background-color: #e0e0e0;\n"
"    border: 1px solid #b0b0b0;\n"
"    padding: 4px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* ================= HEADER FRAME ================= */\n"
"QFrame#frameHeader {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"   ", None))
        self.lblJudul1.setStyleSheet(QCoreApplication.translate("Form", u"font: bold 14pt;", None))
        self.lblJudul1.setText(QCoreApplication.translate("Form", u"APLIKASI SISTEM INFORMASI REGISTER CV", None))
        self.lblJudul2.setStyleSheet(QCoreApplication.translate("Form", u"font: 11pt;", None))
        self.lblJudul2.setText(QCoreApplication.translate("Form", u"PENGADILAN NEGERI KELAS IA PADANG", None))
        self.lblJudul3.setStyleSheet(QCoreApplication.translate("Form", u"font: 10pt;", None))
        self.lblJudul3.setText(QCoreApplication.translate("Form", u"BERBASIS JAVA", None))
        self.lblCari.setStyleSheet(QCoreApplication.translate("Form", u"font: bold 12pt;", None))
        self.lblCari.setText(QCoreApplication.translate("Form", u"PENCARIAN DATA REGISTER", None))
        self.lblFilter.setText(QCoreApplication.translate("Form", u"Masukkan No Register / Nama Pemilik / Kode CV", None))
        self.btnCari.setText(QCoreApplication.translate("Form", u"CARI", None))
        self.btnKeluar.setText(QCoreApplication.translate("Form", u"KELUAR", None))
    # retranslateUi

