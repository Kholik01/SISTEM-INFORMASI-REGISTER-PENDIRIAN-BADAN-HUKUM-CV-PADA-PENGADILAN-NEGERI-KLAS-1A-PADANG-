# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_cv.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 680)
        self.vboxLayout = QVBoxLayout(Form)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.lblJumlah = QLabel(Form)
        self.lblJumlah.setObjectName(u"lblJumlah")
        self.lblJumlah.setMaximumSize(QSize(80, 80))
        self.lblJumlah.setPixmap(QPixmap(u":/logo/logo.png"))

        self.hboxLayout.addWidget(self.lblJumlah)

        self.vboxLayout1 = QVBoxLayout()
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.lblJudul = QLabel(Form)
        self.lblJudul.setObjectName(u"lblJudul")
        self.lblJudul.setAlignment(Qt.AlignCenter)

        self.vboxLayout1.addWidget(self.lblJudul)

        self.lblSub = QLabel(Form)
        self.lblSub.setObjectName(u"lblSub")
        self.lblSub.setAlignment(Qt.AlignCenter)

        self.vboxLayout1.addWidget(self.lblSub)


        self.hboxLayout.addLayout(self.vboxLayout1)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblJumlah1 = QLabel(self.groupBox)
        self.lblJumlah1.setObjectName(u"lblJumlah1")

        self.gridLayout.addWidget(self.lblJumlah1, 0, 0, 1, 1)

        self.txtKodeCV = QLineEdit(self.groupBox)
        self.txtKodeCV.setObjectName(u"txtKodeCV")

        self.gridLayout.addWidget(self.txtKodeCV, 0, 1, 1, 1)

        self.lblJumlah2 = QLabel(self.groupBox)
        self.lblJumlah2.setObjectName(u"lblJumlah2")

        self.gridLayout.addWidget(self.lblJumlah2, 0, 2, 1, 1)

        self.txtModal = QLineEdit(self.groupBox)
        self.txtModal.setObjectName(u"txtModal")

        self.gridLayout.addWidget(self.txtModal, 0, 3, 1, 1)

        self.lblJumlah3 = QLabel(self.groupBox)
        self.lblJumlah3.setObjectName(u"lblJumlah3")

        self.gridLayout.addWidget(self.lblJumlah3, 1, 0, 1, 1)

        self.txtNamaCV = QLineEdit(self.groupBox)
        self.txtNamaCV.setObjectName(u"txtNamaCV")

        self.gridLayout.addWidget(self.txtNamaCV, 1, 1, 1, 1)

        self.lblJumlah4 = QLabel(self.groupBox)
        self.lblJumlah4.setObjectName(u"lblJumlah4")

        self.gridLayout.addWidget(self.lblJumlah4, 1, 2, 1, 1)

        self.dateBerdiri = QDateEdit(self.groupBox)
        self.dateBerdiri.setObjectName(u"dateBerdiri")
        self.dateBerdiri.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateBerdiri, 1, 3, 1, 1)

        self.lblJumlah5 = QLabel(self.groupBox)
        self.lblJumlah5.setObjectName(u"lblJumlah5")

        self.gridLayout.addWidget(self.lblJumlah5, 2, 0, 1, 1)

        self.txtAlamatCV = QTextEdit(self.groupBox)
        self.txtAlamatCV.setObjectName(u"txtAlamatCV")

        self.gridLayout.addWidget(self.txtAlamatCV, 2, 1, 1, 1)

        self.lblJumlah6 = QLabel(self.groupBox)
        self.lblJumlah6.setObjectName(u"lblJumlah6")

        self.gridLayout.addWidget(self.lblJumlah6, 2, 2, 1, 1)

        self.txtJenisUsaha = QTextEdit(self.groupBox)
        self.txtJenisUsaha.setObjectName(u"txtJenisUsaha")

        self.gridLayout.addWidget(self.txtJenisUsaha, 2, 3, 1, 1)


        self.vboxLayout.addWidget(self.groupBox)

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


        self.vboxLayout.addLayout(self.hboxLayout1)

        self.tableCV = QTableWidget(Form)
        if (self.tableCV.columnCount() < 6):
            self.tableCV.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableCV.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableCV.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableCV.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableCV.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableCV.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableCV.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableCV.setObjectName(u"tableCV")
        self.tableCV.setRowCount(0)
        self.tableCV.setColumnCount(6)

        self.vboxLayout.addWidget(self.tableCV)

        self.lblJumlah7 = QLabel(Form)
        self.lblJumlah7.setObjectName(u"lblJumlah7")
        self.lblJumlah7.setAlignment(Qt.AlignRight)

        self.vboxLayout.addWidget(self.lblJumlah7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data CV", None))
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
"QLineEdit, QTextEdit, QDateEdit {\n"
"  "
                        "  background-color: #ffffff;\n"
"    border: 1px solid #a0a0a0;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
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
        self.lblJudul.setText(QCoreApplication.translate("Form", u"APLIKASI SISTEM INFORMASI REGISTER CV", None))
        self.lblSub.setText(QCoreApplication.translate("Form", u"PENGADILAN NEGERI KELAS IA PADANG - BERBASIS JAVA", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"ENTRY DATA CV", None))
        self.lblJumlah1.setText(QCoreApplication.translate("Form", u"Kode CV", None))
        self.lblJumlah2.setText(QCoreApplication.translate("Form", u"Modal", None))
        self.lblJumlah3.setText(QCoreApplication.translate("Form", u"Nama CV", None))
        self.lblJumlah4.setText(QCoreApplication.translate("Form", u"Tanggal Berdiri", None))
        self.lblJumlah5.setText(QCoreApplication.translate("Form", u"Alamat CV", None))
        self.lblJumlah6.setText(QCoreApplication.translate("Form", u"Jenis Usaha", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"Bersih Teks", None))
        self.btnKeluar.setText(QCoreApplication.translate("Form", u"Keluar", None))
        ___qtablewidgetitem = self.tableCV.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Kode CV", None));
        ___qtablewidgetitem1 = self.tableCV.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama CV", None));
        ___qtablewidgetitem2 = self.tableCV.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Alamat CV", None));
        ___qtablewidgetitem3 = self.tableCV.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Modal", None));
        ___qtablewidgetitem4 = self.tableCV.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Tanggal Berdiri", None));
        ___qtablewidgetitem5 = self.tableCV.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Jenis Usaha", None));
        self.lblJumlah7.setText(QCoreApplication.translate("Form", u"JUMLAH DATA CV : 0", None))
    # retranslateUi

