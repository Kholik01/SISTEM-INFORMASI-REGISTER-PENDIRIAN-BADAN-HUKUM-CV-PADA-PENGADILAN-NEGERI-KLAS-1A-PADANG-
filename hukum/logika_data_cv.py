import sys
from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from PySide6.QtWidgets import QAbstractItemView


class DataCV(QWidget):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.init_table()
        self.init_event()
        self.reset_form()
        self.update_jumlah()

    # ================= LOAD UI =================
    def load_ui(self):
        loader = QUiLoader()
        file = QFile("data_cv.ui")
        if not file.open(QFile.ReadOnly):
            QMessageBox.critical(self, "Error", "File data_cv.ui tidak ditemukan!")
            return

        self.ui = loader.load(file, self)
        file.close()

        self.setWindowTitle("Data CV")
        self.setMinimumSize(1000, 680)

    # ================= TABLE =================
    def init_table(self):
        self.ui.tableCV.setColumnCount(6)
        self.ui.tableCV.setHorizontalHeaderLabels([
            "Kode CV",
            "Nama CV",
            "Alamat CV",
            "Modal",
            "Tanggal Berdiri",
            "Jenis Usaha"
        ])
        self.ui.tableCV.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableCV.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # ================= EVENT =================
    def init_event(self):
        self.ui.btnSimpan.clicked.connect(self.simpan_data)
        self.ui.btnUbah.clicked.connect(self.ubah_data)
        self.ui.btnHapus.clicked.connect(self.hapus_data)
        self.ui.btnBersih.clicked.connect(self.reset_form)
        self.ui.btnKeluar.clicked.connect(self.close)
        self.ui.tableCV.cellClicked.connect(self.pilih_data)

    # ================= CRUD =================
    def simpan_data(self):
        kode = self.ui.txtKodeCV.text().strip()
        nama = self.ui.txtNamaCV.text().strip()
        alamat = self.ui.txtAlamatCV.toPlainText().strip()
        modal = self.ui.txtModal.text().strip()
        tanggal = self.ui.dateBerdiri.date().toString("yyyy-MM-dd")
        jenis = self.ui.txtJenisUsaha.toPlainText().strip()

        if not kode or not nama:
            QMessageBox.warning(self, "Peringatan", "Kode CV dan Nama CV wajib diisi!")
            return

        for row in range(self.ui.tableCV.rowCount()):
            if self.ui.tableCV.item(row, 0).text() == kode:
                QMessageBox.warning(self, "Peringatan", "Kode CV sudah ada!")
                return

        row = self.ui.tableCV.rowCount()
        self.ui.tableCV.insertRow(row)

        self.ui.tableCV.setItem(row, 0, QTableWidgetItem(kode))
        self.ui.tableCV.setItem(row, 1, QTableWidgetItem(nama))
        self.ui.tableCV.setItem(row, 2, QTableWidgetItem(alamat))
        self.ui.tableCV.setItem(row, 3, QTableWidgetItem(modal))
        self.ui.tableCV.setItem(row, 4, QTableWidgetItem(tanggal))
        self.ui.tableCV.setItem(row, 5, QTableWidgetItem(jenis))

        QMessageBox.information(self, "Sukses", "Data CV berhasil disimpan")
        self.reset_form()
        self.update_jumlah()

    def pilih_data(self, row, column):
        self.ui.txtKodeCV.setText(self.ui.tableCV.item(row, 0).text())
        self.ui.txtNamaCV.setText(self.ui.tableCV.item(row, 1).text())
        self.ui.txtAlamatCV.setPlainText(self.ui.tableCV.item(row, 2).text())
        self.ui.txtModal.setText(self.ui.tableCV.item(row, 3).text())
        self.ui.dateBerdiri.setDate(
            QDate.fromString(self.ui.tableCV.item(row, 4).text(), "yyyy-MM-dd")
        )
        self.ui.txtJenisUsaha.setPlainText(self.ui.tableCV.item(row, 5).text())

    def ubah_data(self):
        row = self.ui.tableCV.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data dulu!")
            return

        self.ui.tableCV.setItem(row, 1, QTableWidgetItem(self.ui.txtNamaCV.text()))
        self.ui.tableCV.setItem(row, 2, QTableWidgetItem(self.ui.txtAlamatCV.toPlainText()))
        self.ui.tableCV.setItem(row, 3, QTableWidgetItem(self.ui.txtModal.text()))
        self.ui.tableCV.setItem(
            row, 4,
            QTableWidgetItem(self.ui.dateBerdiri.date().toString("yyyy-MM-dd"))
        )
        self.ui.tableCV.setItem(row, 5, QTableWidgetItem(self.ui.txtJenisUsaha.toPlainText()))

        QMessageBox.information(self, "Sukses", "Data CV berhasil diubah")
        self.reset_form()

    def hapus_data(self):
        row = self.ui.tableCV.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data dulu!")
            return

        if QMessageBox.question(
            self, "Konfirmasi",
            "Yakin ingin menghapus data?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            self.ui.tableCV.removeRow(row)
            self.reset_form()
            self.update_jumlah()

    # ================= UTIL =================
    def reset_form(self):
        self.ui.txtKodeCV.clear()
        self.ui.txtNamaCV.clear()
        self.ui.txtAlamatCV.clear()
        self.ui.txtModal.clear()
        self.ui.txtJenisUsaha.clear()
        self.ui.dateBerdiri.setDate(QDate.currentDate())
        self.ui.tableCV.clearSelection()

    def update_jumlah(self):
        jumlah = self.ui.tableCV.rowCount()
        self.ui.lblJumlah.setText(f"JUMLAH DATA CV : {jumlah}")
