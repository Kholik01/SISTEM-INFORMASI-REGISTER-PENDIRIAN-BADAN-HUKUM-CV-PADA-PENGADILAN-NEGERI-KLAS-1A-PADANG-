# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_register_cv.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1028, 717)
        self.vboxLayout = QVBoxLayout(Form)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(80, 80))
        self.label.setPixmap(QPixmap(u":/logo/logo.png"))

        self.hboxLayout.addWidget(self.label)

        self.vboxLayout1 = QVBoxLayout()
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.lblJudul = QLabel(Form)
        self.lblJudul.setObjectName(u"lblJudul")
        self.lblJudul.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout1.addWidget(self.lblJudul)

        self.lblSub = QLabel(Form)
        self.lblSub.setObjectName(u"lblSub")
        self.lblSub.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout1.addWidget(self.lblSub)


        self.hboxLayout.addLayout(self.vboxLayout1)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)

        self.txtNoRegister = QLineEdit(self.groupBox)
        self.txtNoRegister.setObjectName(u"txtNoRegister")

        self.gridLayout.addWidget(self.txtNoRegister, 0, 1, 1, 1)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)

        self.cmbKodeCV = QComboBox(self.groupBox)
        self.cmbKodeCV.setObjectName(u"cmbKodeCV")

        self.gridLayout.addWidget(self.cmbKodeCV, 1, 1, 1, 1)

        self.label3 = QLabel(self.groupBox)
        self.label3.setObjectName(u"label3")

        self.gridLayout.addWidget(self.label3, 2, 0, 1, 1)

        self.txtNamaCV = QLineEdit(self.groupBox)
        self.txtNamaCV.setObjectName(u"txtNamaCV")

        self.gridLayout.addWidget(self.txtNamaCV, 2, 1, 1, 1)

        self.label4 = QLabel(self.groupBox)
        self.label4.setObjectName(u"label4")

        self.gridLayout.addWidget(self.label4, 3, 0, 1, 1)

        self.txtAlamatCV = QTextEdit(self.groupBox)
        self.txtAlamatCV.setObjectName(u"txtAlamatCV")

        self.gridLayout.addWidget(self.txtAlamatCV, 3, 1, 1, 1)

        self.label5 = QLabel(self.groupBox)
        self.label5.setObjectName(u"label5")

        self.gridLayout.addWidget(self.label5, 4, 0, 1, 1)

        self.txtModal = QLineEdit(self.groupBox)
        self.txtModal.setObjectName(u"txtModal")

        self.gridLayout.addWidget(self.txtModal, 4, 1, 1, 1)

        self.label6 = QLabel(self.groupBox)
        self.label6.setObjectName(u"label6")

        self.gridLayout.addWidget(self.label6, 5, 0, 1, 1)

        self.txtJenisUsaha = QTextEdit(self.groupBox)
        self.txtJenisUsaha.setObjectName(u"txtJenisUsaha")

        self.gridLayout.addWidget(self.txtJenisUsaha, 5, 1, 1, 1)

        self.label7 = QLabel(self.groupBox)
        self.label7.setObjectName(u"label7")

        self.gridLayout.addWidget(self.label7, 6, 0, 1, 1)

        self.dateBerdiri = QDateEdit(self.groupBox)
        self.dateBerdiri.setObjectName(u"dateBerdiri")
        self.dateBerdiri.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateBerdiri, 6, 1, 1, 1)

        self.label8 = QLabel(self.groupBox)
        self.label8.setObjectName(u"label8")

        self.gridLayout.addWidget(self.label8, 0, 2, 1, 1)

        self.cmbKodePemilik = QComboBox(self.groupBox)
        self.cmbKodePemilik.setObjectName(u"cmbKodePemilik")

        self.gridLayout.addWidget(self.cmbKodePemilik, 0, 3, 1, 1)

        self.label9 = QLabel(self.groupBox)
        self.label9.setObjectName(u"label9")

        self.gridLayout.addWidget(self.label9, 1, 2, 1, 1)

        self.txtNamaPemilik = QLineEdit(self.groupBox)
        self.txtNamaPemilik.setObjectName(u"txtNamaPemilik")

        self.gridLayout.addWidget(self.txtNamaPemilik, 1, 3, 1, 1)

        self.label10 = QLabel(self.groupBox)
        self.label10.setObjectName(u"label10")

        self.gridLayout.addWidget(self.label10, 2, 2, 1, 1)

        self.cmbKodeNotaris = QComboBox(self.groupBox)
        self.cmbKodeNotaris.setObjectName(u"cmbKodeNotaris")

        self.gridLayout.addWidget(self.cmbKodeNotaris, 2, 3, 1, 1)

        self.label11 = QLabel(self.groupBox)
        self.label11.setObjectName(u"label11")

        self.gridLayout.addWidget(self.label11, 3, 2, 1, 1)

        self.txtNamaNotaris = QLineEdit(self.groupBox)
        self.txtNamaNotaris.setObjectName(u"txtNamaNotaris")

        self.gridLayout.addWidget(self.txtNamaNotaris, 3, 3, 1, 1)

        self.label12 = QLabel(self.groupBox)
        self.label12.setObjectName(u"label12")

        self.gridLayout.addWidget(self.label12, 4, 2, 1, 1)

        self.dateRegister = QDateEdit(self.groupBox)
        self.dateRegister.setObjectName(u"dateRegister")
        self.dateRegister.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateRegister, 4, 3, 1, 1)

        self.label13 = QLabel(self.groupBox)
        self.label13.setObjectName(u"label13")

        self.gridLayout.addWidget(self.label13, 5, 2, 1, 1)

        self.txtJangkaWaktu = QLineEdit(self.groupBox)
        self.txtJangkaWaktu.setObjectName(u"txtJangkaWaktu")

        self.gridLayout.addWidget(self.txtJangkaWaktu, 5, 3, 1, 1)

        self.label14 = QLabel(self.groupBox)
        self.label14.setObjectName(u"label14")

        self.gridLayout.addWidget(self.label14, 6, 2, 1, 1)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.rbBaru = QRadioButton(self.groupBox)
        self.rbBaru.setObjectName(u"rbBaru")

        self.hboxLayout1.addWidget(self.rbBaru)

        self.rbPerubahan = QRadioButton(self.groupBox)
        self.rbPerubahan.setObjectName(u"rbPerubahan")

        self.hboxLayout1.addWidget(self.rbPerubahan)


        self.gridLayout.addLayout(self.hboxLayout1, 6, 3, 1, 1)

        self.label15 = QLabel(self.groupBox)
        self.label15.setObjectName(u"label15")

        self.gridLayout.addWidget(self.label15, 7, 2, 1, 1)

        self.txtKeterangan = QTextEdit(self.groupBox)
        self.txtKeterangan.setObjectName(u"txtKeterangan")

        self.gridLayout.addWidget(self.txtKeterangan, 7, 3, 1, 1)


        self.vboxLayout.addWidget(self.groupBox)

        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.hboxLayout2.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")

        self.hboxLayout2.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")

        self.hboxLayout2.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(Form)
        self.btnBersih.setObjectName(u"btnBersih")

        self.hboxLayout2.addWidget(self.btnBersih)

        self.btnKeluar = QPushButton(Form)
        self.btnKeluar.setObjectName(u"btnKeluar")

        self.hboxLayout2.addWidget(self.btnKeluar)


        self.vboxLayout.addLayout(self.hboxLayout2)

        self.tableRegisterCV = QTableWidget(Form)
        if (self.tableRegisterCV.columnCount() < 10):
            self.tableRegisterCV.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableRegisterCV.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableRegisterCV.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableRegisterCV.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableRegisterCV.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableRegisterCV.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableRegisterCV.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableRegisterCV.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableRegisterCV.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableRegisterCV.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableRegisterCV.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableRegisterCV.setObjectName(u"tableRegisterCV")
        self.tableRegisterCV.setRowCount(0)
        self.tableRegisterCV.setColumnCount(10)

        self.vboxLayout.addWidget(self.tableRegisterCV)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Register CV", None))
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
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QLabel#lblSub {\n"
"    font-size: 12px;\n"
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
"    subcontrol-position: top center;\n"
"    padding: 0 10px;\n"
"}\n"
"\n"
"/* ================= INPUT ================= */\n"
"QLineEdit, QTextEdit, QComboBox, QDateEd"
                        "it {\n"
"    background-color: #ffffff;\n"
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
        self.lblSub.setText(QCoreApplication.translate("Form", u"PENGADILAN NEGERI KELAS IA PADANG", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"ENTRY DATA REGISTER CV", None))
        self.label1.setText(QCoreApplication.translate("Form", u"No Register", None))
        self.label2.setText(QCoreApplication.translate("Form", u"Kode CV", None))
        self.label3.setText(QCoreApplication.translate("Form", u"Nama CV", None))
        self.label4.setText(QCoreApplication.translate("Form", u"Alamat CV", None))
        self.label5.setText(QCoreApplication.translate("Form", u"Modal", None))
        self.label6.setText(QCoreApplication.translate("Form", u"Jenis Usaha", None))
        self.label7.setText(QCoreApplication.translate("Form", u"Tanggal Berdiri", None))
        self.label8.setText(QCoreApplication.translate("Form", u"Kode Pemilik", None))
        self.label9.setText(QCoreApplication.translate("Form", u"Nama Pemilik", None))
        self.label10.setText(QCoreApplication.translate("Form", u"Kode Notaris", None))
        self.label11.setText(QCoreApplication.translate("Form", u"Nama Notaris", None))
        self.label12.setText(QCoreApplication.translate("Form", u"Tanggal Register", None))
        self.label13.setText(QCoreApplication.translate("Form", u"Jangka Waktu", None))
        self.label14.setText(QCoreApplication.translate("Form", u"Status", None))
        self.rbBaru.setText(QCoreApplication.translate("Form", u"CV Baru", None))
        self.rbPerubahan.setText(QCoreApplication.translate("Form", u"Perubahan", None))
        self.label15.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"Bersih Teks", None))
        self.btnKeluar.setText(QCoreApplication.translate("Form", u"Keluar", None))
        ___qtablewidgetitem = self.tableRegisterCV.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"No Reg", None));
        ___qtablewidgetitem1 = self.tableRegisterCV.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Kode CV", None));
        ___qtablewidgetitem2 = self.tableRegisterCV.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Nama CV", None));
        ___qtablewidgetitem3 = self.tableRegisterCV.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Nama Pemilik", None));
        ___qtablewidgetitem4 = self.tableRegisterCV.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Nama Notaris", None));
        ___qtablewidgetitem5 = self.tableRegisterCV.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Tgl Register", None));
        ___qtablewidgetitem6 = self.tableRegisterCV.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Status", None));
        ___qtablewidgetitem7 = self.tableRegisterCV.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Jangka Waktu", None));
        ___qtablewidgetitem8 = self.tableRegisterCV.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Keterangan", None));
        ___qtablewidgetitem9 = self.tableRegisterCV.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Modal", None));
    # retranslateUi

