from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from DataBase import DataBase


class LogikaDataNotaris(QWidget):
    def __init__(self):
        super().__init__()
        self.db = DataBase()
        self.load_ui()
        self.setup_table()
        self.load_data()
        self.setup_event()

    def load_ui(self):
        loader = QUiLoader()
        file = QFile("data_notaris.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()
        self.setWindowTitle("Data Notaris")
        self.resize(900, 600)

    def setup_table(self):
        self.ui.tableNotaris.setColumnCount(5)
        self.ui.tableNotaris.setHorizontalHeaderLabels(
            ["Kode", "Nama", "JK", "Alamat", "No Telp"]
        )
        self.ui.tableNotaris.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableNotaris.setSelectionMode(QAbstractItemView.SingleSelection)

    def load_data(self):
        self.ui.tableNotaris.setRowCount(0)
        data = self.db.ambil_semua_notaris()
        for row, d in enumerate(data):
            self.ui.tableNotaris.insertRow(row)
            for col, val in enumerate(d):
                self.ui.tableNotaris.setItem(row, col, QTableWidgetItem(str(val)))

    def setup_event(self):
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)
        self.ui.btnKeluar.clicked.connect(self.close)
        self.ui.tableNotaris.cellClicked.connect(self.pilih)

    def simpan(self):
        kd = self.ui.txtKode.text()
        nama = self.ui.txtNama.text()
        jk = "L" if self.ui.rbL.isChecked() else "P"
        alamat = self.ui.txtAlamat.text()
        telp = self.ui.txtTelp.text()

        if not kd or not nama:
            QMessageBox.warning(self, "Peringatan", "Data wajib diisi")
            return

        self.db.tambah_notaris(kd, nama, jk, alamat, telp)
        QMessageBox.information(self, "Sukses", "Data berhasil disimpan")
        self.load_data()
        self.bersih()

    def ubah(self):
        self.db.ubah_notaris(
            self.ui.txtKode.text(),
            self.ui.txtNama.text(),
            "L" if self.ui.rbL.isChecked() else "P",
            self.ui.txtAlamat.text(),
            self.ui.txtTelp.text()
        )
        QMessageBox.information(self, "Sukses", "Data berhasil diubah")
        self.load_data()

    def hapus(self):
        self.db.hapus_notaris(self.ui.txtKode.text())
        QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
        self.load_data()
        self.bersih()

    def pilih(self, row, _):
        self.ui.txtKode.setText(self.ui.tableNotaris.item(row, 0).text())
        self.ui.txtNama.setText(self.ui.tableNotaris.item(row, 1).text())
        jk = self.ui.tableNotaris.item(row, 2).text()
        self.ui.rbL.setChecked(jk == "L")
        self.ui.rbP.setChecked(jk == "P")
        self.ui.txtAlamat.setText(self.ui.tableNotaris.item(row, 3).text())
        self.ui.txtTelp.setText(self.ui.tableNotaris.item(row, 4).text())

    def bersih(self):
        self.ui.txtKode.clear()
        self.ui.txtNama.clear()
        self.ui.txtAlamat.clear()
        self.ui.txtTelp.clear()
        self.ui.rbL.setChecked(True)
