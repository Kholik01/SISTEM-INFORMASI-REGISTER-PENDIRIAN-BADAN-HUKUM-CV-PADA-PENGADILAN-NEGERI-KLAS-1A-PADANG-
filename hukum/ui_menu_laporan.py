# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_laporan.ui'
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
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 600)
        self.vboxLayout = QVBoxLayout(Form)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.hboxLayout = QHBoxLayout(self.frame)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 90))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hboxLayout.addWidget(self.label)

        self.label1 = QLabel(self.frame)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hboxLayout.addWidget(self.label1)


        self.vboxLayout.addWidget(self.frame)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnCetakCV = QPushButton(self.groupBox)
        self.btnCetakCV.setObjectName(u"btnCetakCV")

        self.gridLayout.addWidget(self.btnCetakCV, 0, 1, 1, 1)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)

        self.rbCV = QRadioButton(self.groupBox)
        self.rbCV.setObjectName(u"rbCV")

        self.gridLayout.addWidget(self.rbCV, 0, 0, 1, 1)

        self.cbBulan = QComboBox(self.groupBox)
        self.cbBulan.setObjectName(u"cbBulan")

        self.gridLayout.addWidget(self.cbBulan, 1, 1, 1, 1)

        self.cbTahun = QComboBox(self.groupBox)
        self.cbTahun.setObjectName(u"cbTahun")

        self.gridLayout.addWidget(self.cbTahun, 2, 1, 1, 1)

        self.label3 = QLabel(self.groupBox)
        self.label3.setObjectName(u"label3")

        self.gridLayout.addWidget(self.label3, 2, 0, 1, 1)


        self.hboxLayout1.addWidget(self.groupBox)

        self.groupBox1 = QGroupBox(Form)
        self.groupBox1.setObjectName(u"groupBox1")
        self.gridLayout1 = QGridLayout(self.groupBox1)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.rbPerHari = QRadioButton(self.groupBox1)
        self.rbPerHari.setObjectName(u"rbPerHari")

        self.gridLayout1.addWidget(self.rbPerHari, 0, 0, 1, 1)

        self.cbBulan2 = QComboBox(self.groupBox1)
        self.cbBulan2.setObjectName(u"cbBulan2")

        self.gridLayout1.addWidget(self.cbBulan2, 0, 1, 1, 1)

        self.rbPerBulan = QRadioButton(self.groupBox1)
        self.rbPerBulan.setObjectName(u"rbPerBulan")

        self.gridLayout1.addWidget(self.rbPerBulan, 1, 0, 1, 1)

        self.cbBulan3 = QComboBox(self.groupBox1)
        self.cbBulan3.setObjectName(u"cbBulan3")

        self.gridLayout1.addWidget(self.cbBulan3, 1, 1, 1, 1)

        self.cbTahun2 = QComboBox(self.groupBox1)
        self.cbTahun2.setObjectName(u"cbTahun2")

        self.gridLayout1.addWidget(self.cbTahun2, 1, 2, 1, 1)

        self.rbPerTahun = QRadioButton(self.groupBox1)
        self.rbPerTahun.setObjectName(u"rbPerTahun")

        self.gridLayout1.addWidget(self.rbPerTahun, 2, 0, 1, 1)

        self.cbTahun3 = QComboBox(self.groupBox1)
        self.cbTahun3.setObjectName(u"cbTahun3")

        self.gridLayout1.addWidget(self.cbTahun3, 2, 1, 1, 1)

        self.btnLihatTahun = QPushButton(self.groupBox1)
        self.btnLihatTahun.setObjectName(u"btnLihatTahun")

        self.gridLayout1.addWidget(self.btnLihatTahun, 2, 2, 1, 1)


        self.hboxLayout1.addWidget(self.groupBox1)


        self.vboxLayout.addLayout(self.hboxLayout1)

        self.groupBox2 = QGroupBox(Form)
        self.groupBox2.setObjectName(u"groupBox2")
        self.hboxLayout2 = QHBoxLayout(self.groupBox2)
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.label4 = QLabel(self.groupBox2)
        self.label4.setObjectName(u"label4")

        self.hboxLayout2.addWidget(self.label4)

        self.tableWidget = QTableWidget(self.groupBox2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.hboxLayout2.addWidget(self.tableWidget)

        self.btnCetakStatus = QPushButton(self.groupBox2)
        self.btnCetakStatus.setObjectName(u"btnCetakStatus")

        self.hboxLayout2.addWidget(self.btnCetakStatus)


        self.vboxLayout.addWidget(self.groupBox2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Menu Laporan", None))
        Form.setStyleSheet(QCoreApplication.translate("Form", u"\n"
"QWidget {\n"
"    background-color: #f2f2f2;\n"
"    font-family: Arial;\n"
"    font-size: 10pt;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #b0b0b0;\n"
"    border-radius: 4px;\n"
"    margin-top: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"}\n"
"\n"
"QLabel { color: #000000; }\n"
"\n"
"QPushButton {\n"
"    background-color: #e6e6e6;\n"
"    border: 1px solid #8a8a8a;\n"
"    border-radius: 3px;\n"
"    padding: 6px 16px;\n"
"    min-height: 28px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover { background-color: #dcdcdc; }\n"
"QPushButton:pressed { background-color: #cfcfcf; }\n"
"\n"
"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #8a8a8a;\n"
"    padding: 4px 6px;\n"
"    min-height: 26px;\n"
"}\n"
"\n"
"QRadioButton { spacing: 6px; }\n"
"   ", None))
        self.frame.setStyleSheet(QCoreApplication.translate("Form", u"background-color:#e0e0e0;", None))
        self.label.setText(QCoreApplication.translate("Form", u"LOGO", None))
        self.label1.setText(QCoreApplication.translate("Form", u"\n"
"APLIKASI SISTEM INFORMASI REGISTER CV\n"
"PENGADILAN NEGERI KLAS IA PADANG\n"
"BERBASIS JAVA\n"
"Jl. Khatib Sulaiman No.80 Padang\n"
"         ", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"CV, PEMILIK, NOTARIS & REGISTER", None))
        self.btnCetakCV.setText(QCoreApplication.translate("Form", u"CETAK", None))
        self.label2.setText(QCoreApplication.translate("Form", u"BULAN", None))
        self.rbCV.setText(QCoreApplication.translate("Form", u"LAPORAN KESELURUHAN", None))
        self.label3.setText(QCoreApplication.translate("Form", u"TAHUN", None))
        self.groupBox1.setTitle(QCoreApplication.translate("Form", u"LAPORAN REGISTER PERTAHUN, PERBULAN, PERHARI", None))
        self.rbPerHari.setText(QCoreApplication.translate("Form", u"PERHARI", None))
        self.rbPerBulan.setText(QCoreApplication.translate("Form", u"PERBULAN", None))
        self.rbPerTahun.setText(QCoreApplication.translate("Form", u"PERTAHUN", None))
        self.btnLihatTahun.setText(QCoreApplication.translate("Form", u"LIHAT LAPORAN", None))
        self.groupBox2.setTitle(QCoreApplication.translate("Form", u"LAPORAN STATUS CV", None))
        self.label4.setText(QCoreApplication.translate("Form", u"PILIH LAPORAN", None))
        self.btnCetakStatus.setText(QCoreApplication.translate("Form", u"CETAK", None))
    # retranslateUi

