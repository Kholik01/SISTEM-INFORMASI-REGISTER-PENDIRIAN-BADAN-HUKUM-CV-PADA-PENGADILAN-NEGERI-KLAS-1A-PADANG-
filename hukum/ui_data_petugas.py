# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_petugas.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 600)
        self.vboxLayout = QVBoxLayout(Form)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.lblJudul = QLabel(Form)
        self.lblJudul.setObjectName(u"lblJudul")
        self.lblJudul.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.lblJudul)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.txtId = QLineEdit(self.groupBox)
        self.txtId.setObjectName(u"txtId")

        self.gridLayout.addWidget(self.txtId, 0, 1, 1, 1)

        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 0, 2, 1, 1)

        self.txtNama = QLineEdit(self.groupBox)
        self.txtNama.setObjectName(u"txtNama")

        self.gridLayout.addWidget(self.txtNama, 0, 3, 1, 1)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)

        self.txtUser = QLineEdit(self.groupBox)
        self.txtUser.setObjectName(u"txtUser")

        self.gridLayout.addWidget(self.txtUser, 1, 1, 1, 1)

        self.label3 = QLabel(self.groupBox)
        self.label3.setObjectName(u"label3")

        self.gridLayout.addWidget(self.label3, 1, 2, 1, 1)

        self.txtPass = QLineEdit(self.groupBox)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.txtPass, 1, 3, 1, 1)


        self.vboxLayout.addWidget(self.groupBox)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.hboxLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")

        self.hboxLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")

        self.hboxLayout.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(Form)
        self.btnBersih.setObjectName(u"btnBersih")

        self.hboxLayout.addWidget(self.btnBersih)

        self.btnKeluar = QPushButton(Form)
        self.btnKeluar.setObjectName(u"btnKeluar")

        self.hboxLayout.addWidget(self.btnKeluar)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.tablePetugas = QTableWidget(Form)
        if (self.tablePetugas.columnCount() < 4):
            self.tablePetugas.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablePetugas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablePetugas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablePetugas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablePetugas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tablePetugas.setObjectName(u"tablePetugas")
        self.tablePetugas.setColumnCount(4)

        self.vboxLayout.addWidget(self.tablePetugas)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data Petugas", None))
        Form.setStyleSheet(QCoreApplication.translate("Form", u"\n"
"/* ================= GLOBAL ================= */\n"
"QWidget {\n"
"    background-color: #f2f2f2;\n"
"    font-family: Arial;\n"
"    font-size: 11px;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* ================= JUDUL ================= */\n"
"QLabel#lblJudul {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* ================= LABEL ================= */\n"
"QLabel {\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* ================= GROUP BOX ================= */\n"
"QGroupBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #b0b0b0;\n"
"    border-radius: 4px;\n"
"    margin-top: 15px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"}\n"
"\n"
"/* ================= INPUT ================= */\n"
"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #a0a0a0;\n"
"    border-radius: 4px;\n"
"    paddin"
                        "g: 4px;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* ================= BUTTON ================= */\n"
"QPushButton {\n"
"    background-color: #e6e6e6;\n"
"    border: 1px solid #8a8a8a;\n"
"    border-radius: 4px;\n"
"    padding: 6px 14px;\n"
"    font-weight: bold;\n"
"    color: #000000;\n"
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
"/* ================= TABLE ================= */\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    gridline-color: #c0c0c0;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #e0e0e0;\n"
"    border: 1px solid #b0b0b0;\n"
"    padding: 4px;\n"
"    font-weight: bold;\n"
"}\n"
"   ", None))
        self.lblJudul.setText(QCoreApplication.translate("Form", u"ENTRY DATA PETUGAS", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"INPUT DATA", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID ADMIN", None))
        self.label1.setText(QCoreApplication.translate("Form", u"NAMA ADMIN", None))
        self.label2.setText(QCoreApplication.translate("Form", u"USERNAME", None))
        self.label3.setText(QCoreApplication.translate("Form", u"PASSWORD", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        self.btnKeluar.setText(QCoreApplication.translate("Form", u"KELUAR", None))
        ___qtablewidgetitem = self.tablePetugas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tablePetugas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tablePetugas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Username", None));
        ___qtablewidgetitem3 = self.tablePetugas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Password", None));
    # retranslateUi

