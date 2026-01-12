# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Data_Pemilik.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 600)
        Form.setStyleSheet(u"\n"
"/* ================= GLOBAL ================= */\n"
"QWidget {\n"
"    background-color: #f2f2f2;\n"
"    font-family: \"Segoe UI\";\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* ================= LABEL ================= */\n"
"QLabel {\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* ================= INPUT ================= */\n"
"QLineEdit, QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #a0a0a0;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* ================= BUTTON ================= */\n"
"QPushButton {\n"
"    background-color: #e6e6e6;\n"
"    color: #000000;\n"
"    border: 1px solid #8a8a8a;\n"
"    border-radius: 4px;\n"
"    padding: 6px 14px;\n"
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
"/* ================= FRAME FORM ================= */\n"
"QFrame#frameForm {\n"
"    bac"
                        "kground-color: #ffffff;\n"
"    border: 1px solid #b0b0b0;\n"
"    border-radius: 4px;\n"
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
"   ")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblHeader = QLabel(Form)
        self.lblHeader.setObjectName(u"lblHeader")
        self.lblHeader.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lblHeader.setFont(font)

        self.verticalLayout.addWidget(self.lblHeader)

        self.frameForm = QFrame(Form)
        self.frameForm.setObjectName(u"frameForm")
        self.frameForm.setFrameShape(QFrame.StyledPanel)
        self.frameForm.setStyleSheet(u"background-color: #29b330ff;")
        self.gridLayout = QGridLayout(self.frameForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblID = QLabel(self.frameForm)
        self.lblID.setObjectName(u"lblID")

        self.gridLayout.addWidget(self.lblID, 0, 0, 1, 1)

        self.txtID = QLineEdit(self.frameForm)
        self.txtID.setObjectName(u"txtID")

        self.gridLayout.addWidget(self.txtID, 0, 1, 1, 1)

        self.lblAlamat = QLabel(self.frameForm)
        self.lblAlamat.setObjectName(u"lblAlamat")

        self.gridLayout.addWidget(self.lblAlamat, 0, 2, 1, 1)

        self.txtAlamat = QLineEdit(self.frameForm)
        self.txtAlamat.setObjectName(u"txtAlamat")

        self.gridLayout.addWidget(self.txtAlamat, 0, 3, 1, 1)

        self.lblNama = QLabel(self.frameForm)
        self.lblNama.setObjectName(u"lblNama")

        self.gridLayout.addWidget(self.lblNama, 1, 0, 1, 1)

        self.txtNama = QLineEdit(self.frameForm)
        self.txtNama.setObjectName(u"txtNama")

        self.gridLayout.addWidget(self.txtNama, 1, 1, 1, 1)

        self.lblTelp = QLabel(self.frameForm)
        self.lblTelp.setObjectName(u"lblTelp")

        self.gridLayout.addWidget(self.lblTelp, 1, 2, 1, 1)

        self.txtTelp = QLineEdit(self.frameForm)
        self.txtTelp.setObjectName(u"txtTelp")

        self.gridLayout.addWidget(self.txtTelp, 1, 3, 1, 1)

        self.lblJK = QLabel(self.frameForm)
        self.lblJK.setObjectName(u"lblJK")

        self.gridLayout.addWidget(self.lblJK, 2, 0, 1, 1)

        self.cmbJK = QComboBox(self.frameForm)
        self.cmbJK.addItem("")
        self.cmbJK.addItem("")
        self.cmbJK.setObjectName(u"cmbJK")

        self.gridLayout.addWidget(self.cmbJK, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.frameForm)

        self.layoutButtons = QHBoxLayout()
        self.layoutButtons.setObjectName(u"layoutButtons")
        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.layoutButtons.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")

        self.layoutButtons.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")

        self.layoutButtons.addWidget(self.btnHapus)

        self.btnBersih = QPushButton(Form)
        self.btnBersih.setObjectName(u"btnBersih")

        self.layoutButtons.addWidget(self.btnBersih)

        self.btnKeluar = QPushButton(Form)
        self.btnKeluar.setObjectName(u"btnKeluar")

        self.layoutButtons.addWidget(self.btnKeluar)


        self.verticalLayout.addLayout(self.layoutButtons)

        self.tableData = QTableWidget(Form)
        if (self.tableData.columnCount() < 5):
            self.tableData.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableData.setObjectName(u"tableData")

        self.verticalLayout.addWidget(self.tableData)

        self.layoutJumlah = QHBoxLayout()
        self.layoutJumlah.setObjectName(u"layoutJumlah")
        self.lblJumlah = QLabel(Form)
        self.lblJumlah.setObjectName(u"lblJumlah")

        self.layoutJumlah.addWidget(self.lblJumlah)

        self.txtJumlah = QLineEdit(Form)
        self.txtJumlah.setObjectName(u"txtJumlah")
        self.txtJumlah.setReadOnly(True)

        self.layoutJumlah.addWidget(self.txtJumlah)


        self.verticalLayout.addLayout(self.layoutJumlah)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data Pemilik", None))
        self.lblHeader.setText(QCoreApplication.translate("Form", u"APLIKASI SISTEM INFORMASI REGISTER CV\n"
"PENGADILAN NEGERI KELAS 1A PADANG\n"
"BERBASIS JAVA", None))
        self.lblID.setText(QCoreApplication.translate("Form", u"ID Pemilik:", None))
        self.lblAlamat.setText(QCoreApplication.translate("Form", u"Alamat:", None))
        self.lblNama.setText(QCoreApplication.translate("Form", u"Nama Pemilik:", None))
        self.lblTelp.setText(QCoreApplication.translate("Form", u"No Telepon:", None))
        self.lblJK.setText(QCoreApplication.translate("Form", u"Jenis Kelamin:", None))
        self.cmbJK.setItemText(0, QCoreApplication.translate("Form", u"L", None))
        self.cmbJK.setItemText(1, QCoreApplication.translate("Form", u"P", None))

        self.btnSimpan.setText(QCoreApplication.translate("Form", u"&Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"&Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"&Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("Form", u"&Bersih Teks", None))
        self.btnKeluar.setText(QCoreApplication.translate("Form", u"&Keluar", None))
        ___qtablewidgetitem = self.tableData.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Kode Pemilik", None));
        ___qtablewidgetitem1 = self.tableData.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Pemilik", None));
        ___qtablewidgetitem2 = self.tableData.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None));
        ___qtablewidgetitem3 = self.tableData.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Alamat Pemilik", None));
        ___qtablewidgetitem4 = self.tableData.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"No Telepon", None));
        self.lblJumlah.setText(QCoreApplication.translate("Form", u"Jumlah Data Pemilik:", None))
    # retranslateUi

