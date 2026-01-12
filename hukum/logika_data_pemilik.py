from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from DataBase import DataBase


class LogikaDataPemilik(QWidget):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.db = DataBase()
        self.connect_signal()
        self.load_data()

    # =================================================
    # LOAD UI
    # =================================================
    def load_ui(self):
        loader = QUiLoader()
        ui_file = QFile("data_pemilik.ui")

        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError("data_pemilik.ui tidak ditemukan")

        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.setWindowTitle("Data Pemilik")
        self.resize(950, 600)

    # =================================================
    # CONNECT SIGNAL
    # =================================================
    def connect_signal(self):
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)
        self.ui.btnKeluar.clicked.connect(self.close)

    # =================================================
    # LOAD DATA
    # =================================================
    def load_data(self):
        data = self.db.ambil_semua_pemilik()
        self.ui.tableData.setRowCount(0)

        for row_number, row_data in enumerate(data):
            self.ui.tableData.insertRow(row_number)
            for col, value in enumerate(row_data):
                self.ui.tableData.setItem(
                    row_number, col, QTableWidgetItem(str(value))
                )

        self.ui.txtJumlah.setText(str(len(data)))

    # =================================================
    # CRUD
    # =================================================
    def simpan(self):
        kd = self.ui.txtID.text().strip()
        nama = self.ui.txtNama.text().strip()
        jk = self.ui.cmbJK.currentText()
        alamat = self.ui.txtAlamat.text().strip()
        telp = self.ui.txtTelp.text().strip()

        if not kd or not nama:
            QMessageBox.warning(self, "Peringatan", "Kode dan Nama wajib diisi!")
            return

        try:
            self.db.tambah_pemilik(kd, nama, jk, alamat, telp)
            QMessageBox.information(self, "Sukses", "Data berhasil disimpan!")
            self.load_data()
            self.bersih()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data:\n{e}")

    def ubah(self):
        kd = self.ui.txtID.text().strip()
        nama = self.ui.txtNama.text().strip()
        jk = self.ui.cmbJK.currentText()
        alamat = self.ui.txtAlamat.text().strip()
        telp = self.ui.txtTelp.text().strip()

        try:
            self.db.ubah_pemilik(kd, nama, jk, alamat, telp)
            QMessageBox.information(self, "Sukses", "Data berhasil diperbarui!")
            self.load_data()
            self.bersih()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengubah data:\n{e}")

    def hapus(self):
        kd = self.ui.txtID.text().strip()
        if not kd:
            QMessageBox.warning(self, "Peringatan", "Masukkan ID pemilik!")
            return

        try:
            self.db.hapus_pemilik(kd)
            QMessageBox.information(self, "Sukses", "Data berhasil dihapus!")
            self.load_data()
            self.bersih()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menghapus data:\n{e}")

    def bersih(self):
        self.ui.txtID.clear()
        self.ui.txtNama.clear()
        self.ui.txtAlamat.clear()
        self.ui.txtTelp.clear()
        self.ui.cmbJK.setCurrentIndex(0)


# =================================================
# ALIAS (BIAR KONSISTEN DENGAN show_form)
# =================================================
DataPemilik = LogikaDataPemilik

