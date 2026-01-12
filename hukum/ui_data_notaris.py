# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_notaris.ui'
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
    QRadioButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 650)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.lblJudul = QLabel(Form)
        self.lblJudul.setObjectName(u"lblJudul")
        self.lblJudul.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.lblJudul)

        self.lblSub = QLabel(Form)
        self.lblSub.setObjectName(u"lblSub")
        self.lblSub.setAlignment(Qt.AlignCenter)

        self.vboxLayout.addWidget(self.lblSub)


        self.verticalLayout.addLayout(self.vboxLayout)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.txtKode = QLineEdit(self.groupBox)
        self.txtKode.setObjectName(u"txtKode")

        self.gridLayout.addWidget(self.txtKode, 0, 1, 1, 1)

        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 0, 2, 1, 1)

        self.txtAlamat = QLineEdit(self.groupBox)
        self.txtAlamat.setObjectName(u"txtAlamat")

        self.gridLayout.addWidget(self.txtAlamat, 0, 3, 1, 1)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)

        self.txtNama = QLineEdit(self.groupBox)
        self.txtNama.setObjectName(u"txtNama")

        self.gridLayout.addWidget(self.txtNama, 1, 1, 1, 1)

        self.label3 = QLabel(self.groupBox)
        self.label3.setObjectName(u"label3")

        self.gridLayout.addWidget(self.label3, 1, 2, 1, 1)

        self.txtTelp = QLineEdit(self.groupBox)
        self.txtTelp.setObjectName(u"txtTelp")

        self.gridLayout.addWidget(self.txtTelp, 1, 3, 1, 1)

        self.label4 = QLabel(self.groupBox)
        self.label4.setObjectName(u"label4")

        self.gridLayout.addWidget(self.label4, 2, 0, 1, 1)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.rbL = QRadioButton(self.groupBox)
        self.rbL.setObjectName(u"rbL")

        self.hboxLayout.addWidget(self.rbL)

        self.rbP = QRadioButton(self.groupBox)
        self.rbP.setObjectName(u"rbP")

        self.hboxLayout.addWidget(self.rbP)


        self.gridLayout.addLayout(self.hboxLayout, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.hboxLayout1.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")

        self.hboxLayout1.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")

        self.hboxLayout1.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(Form)
        self.btnBersih.setObjectName(u"btnBersih")

        self.hboxLayout1.addWidget(self.btnBersih)

        self.btnKeluar = QPushButton(Form)
        self.btnKeluar.setObjectName(u"btnKeluar")

        self.hboxLayout1.addWidget(self.btnKeluar)


        self.verticalLayout.addLayout(self.hboxLayout1)

        self.tableNotaris = QTableWidget(Form)
        if (self.tableNotaris.columnCount() < 5):
            self.tableNotaris.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableNotaris.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableNotaris.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableNotaris.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableNotaris.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableNotaris.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableNotaris.setObjectName(u"tableNotaris")
        self.tableNotaris.setColumnCount(5)
        self.tableNotaris.setRowCount(0)

        self.verticalLayout.addWidget(self.tableNotaris)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data Notaris", None))
        Form.setStyleSheet(QCoreApplication.translate("Form", u"\n"
"/* ================= GLOBAL ================= */\n"
"QWidget {\n"
"    background-color: #f2f2f2;\n"
"    font-family: Arial;\n"
"    font-size: 11px;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* ================= HEADER ================= */\n"
"QLabel#lblJudul {\n"
"    color: #000000;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel#lblSub {\n"
"    color: #000000;\n"
"    font-size: 12px;\n"
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
"    subcontrol-position: top center;\n"
"    padding: 0 10px;\n"
"}\n"
"\n"
"/* ================= INPUT ================= */\n"
"QLineEdit {\n"
"    background-color: #f"
                        "fffff;\n"
"    border: 1px solid #a0a0a0;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* ================= RADIO BUTTON ================= */\n"
"QRadioButton {\n"
"    color: #000000;\n"
"    spacing: 6px;\n"
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
        self.lblJudul.setText(QCoreApplication.translate("Form", u"APLIKASI SISTEM INFORMASI REGISTER CV", None))
        self.lblSub.setText(QCoreApplication.translate("Form", u"PENGADILAN NEGERI KLAS IA PADANG - BERBASIS JAVA", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"ENTRY DATA NOTARIS", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kode Notaris", None))
        self.label1.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.label2.setText(QCoreApplication.translate("Form", u"Nama Notaris", None))
        self.label3.setText(QCoreApplication.translate("Form", u"No Telp", None))
        self.label4.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None))
        self.rbL.setText(QCoreApplication.translate("Form", u"L", None))
        self.rbP.setText(QCoreApplication.translate("Form", u"P", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"Bersih Teks", None))
        self.btnKeluar.setText(QCoreApplication.translate("Form", u"Keluar", None))
        ___qtablewidgetitem = self.tableNotaris.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Kode", None));
        ___qtablewidgetitem1 = self.tableNotaris.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tableNotaris.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"JK", None));
        ___qtablewidgetitem3 = self.tableNotaris.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Alamat", None));
        ___qtablewidgetitem4 = self.tableNotaris.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"No Telp", None));
    # retranslateUi

