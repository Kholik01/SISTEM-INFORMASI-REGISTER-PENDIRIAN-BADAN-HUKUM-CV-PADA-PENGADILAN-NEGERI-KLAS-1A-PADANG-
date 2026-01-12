from PySide6.QtWidgets import (
    QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate


class DataRegisterCV(QWidget):
    def __init__(self):
        super().__init__()

        self.load_ui()
        self.init_table()
        self.init_event()
        self.init_default()
        self.load_dummy_combo()

    # ================= LOAD UI =================
    def load_ui(self):
        loader = QUiLoader()
        file = QFile("data_register_cv.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

        self.setWindowTitle("Register CV")
        self.resize(1050, 720)

    # ================= INIT DEFAULT =================
    def init_default(self):
        self.ui.dateRegister.setDate(QDate.currentDate())
        self.ui.dateBerdiri.setDate(QDate.currentDate())
        self.ui.rbBaru.setChecked(True)

    def load_dummy_combo(self):
        # Dummy sementara (nanti ganti dari DB)
        self.ui.cmbKodeCV.addItems(["CV001", "CV002", "CV003"])
        self.ui.cmbKodePemilik.addItems(["P001", "P002", "P003"])
        self.ui.cmbKodeNotaris.addItems(["N001", "N002", "N003"])

    # ================= TABLE =================
    def init_table(self):
        table = self.ui.tableRegisterCV
        table.setColumnCount(10)
        table.setHorizontalHeaderLabels([
            "No Reg",
            "Kode CV",
            "Nama CV",
            "Nama Pemilik",
            "Nama Notaris",
            "Tgl Register",
            "Status",
            "Jangka Waktu",
            "Keterangan",
            "Modal"
        ])

        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # ================= EVENT =================
    def init_event(self):
        self.ui.btnSimpan.clicked.connect(self.simpan_data)
        self.ui.btnUbah.clicked.connect(self.ubah_data)
        self.ui.btnHapus.clicked.connect(self.hapus_data)
        self.ui.btnBersih.clicked.connect(self.reset_form)
        self.ui.btnKeluar.clicked.connect(self.close)
        self.ui.tableRegisterCV.cellClicked.connect(self.pilih_data)

    # ================= CRUD =================
    def simpan_data(self):
        no_reg = self.ui.txtNoRegister.text().strip()
        kode_cv = self.ui.cmbKodeCV.currentText()
        nama_cv = self.ui.txtNamaCV.text().strip()
        nama_pemilik = self.ui.txtNamaPemilik.text().strip()
        nama_notaris = self.ui.txtNamaNotaris.text().strip()
        tgl_reg = self.ui.dateRegister.date().toString("yyyy-MM-dd")
        status = "CV Baru" if self.ui.rbBaru.isChecked() else "Perubahan"
        jangka = self.ui.txtJangkaWaktu.text().strip()
        ket = self.ui.txtKeterangan.toPlainText().strip()
        modal = self.ui.txtModal.text().strip()

        if not no_reg or not nama_cv:
            QMessageBox.warning(self, "Peringatan", "No Register dan Nama CV wajib diisi!")
            return

        # cek duplikasi
        for row in range(self.ui.tableRegisterCV.rowCount()):
            if self.ui.tableRegisterCV.item(row, 0).text() == no_reg:
                QMessageBox.warning(self, "Peringatan", "No Register sudah terdaftar!")
                return

        row = self.ui.tableRegisterCV.rowCount()
        self.ui.tableRegisterCV.insertRow(row)

        data = [
            no_reg, kode_cv, nama_cv, nama_pemilik, nama_notaris,
            tgl_reg, status, jangka, ket, modal
        ]

        for col, value in enumerate(data):
            self.ui.tableRegisterCV.setItem(row, col, QTableWidgetItem(value))

        QMessageBox.information(self, "Sukses", "Data Register CV berhasil disimpan")
        self.reset_form()

    def pilih_data(self, row, _):
        table = self.ui.tableRegisterCV

        self.ui.txtNoRegister.setText(table.item(row, 0).text())
        self.ui.cmbKodeCV.setCurrentText(table.item(row, 1).text())
        self.ui.txtNamaCV.setText(table.item(row, 2).text())
        self.ui.txtNamaPemilik.setText(table.item(row, 3).text())
        self.ui.txtNamaNotaris.setText(table.item(row, 4).text())
        self.ui.dateRegister.setDate(
            QDate.fromString(table.item(row, 5).text(), "yyyy-MM-dd")
        )

        status = table.item(row, 6).text()
        self.ui.rbBaru.setChecked(status == "CV Baru")
        self.ui.rbPerubahan.setChecked(status == "Perubahan")

        self.ui.txtJangkaWaktu.setText(table.item(row, 7).text())
        self.ui.txtKeterangan.setPlainText(table.item(row, 8).text())
        self.ui.txtModal.setText(table.item(row, 9).text())

    def ubah_data(self):
        row = self.ui.tableRegisterCV.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu!")
            return

        table = self.ui.tableRegisterCV
        table.setItem(row, 2, QTableWidgetItem(self.ui.txtNamaCV.text()))
        table.setItem(row, 3, QTableWidgetItem(self.ui.txtNamaPemilik.text()))
        table.setItem(row, 4, QTableWidgetItem(self.ui.txtNamaNotaris.text()))
        table.setItem(
            row, 5,
            QTableWidgetItem(self.ui.dateRegister.date().toString("yyyy-MM-dd"))
        )
        status = "CV Baru" if self.ui.rbBaru.isChecked() else "Perubahan"
        table.setItem(row, 6, QTableWidgetItem(status))
        table.setItem(row, 7, QTableWidgetItem(self.ui.txtJangkaWaktu.text()))
        table.setItem(row, 8, QTableWidgetItem(self.ui.txtKeterangan.toPlainText()))
        table.setItem(row, 9, QTableWidgetItem(self.ui.txtModal.text()))

        QMessageBox.information(self, "Sukses", "Data Register CV berhasil diubah")
        self.reset_form()

    def hapus_data(self):
        row = self.ui.tableRegisterCV.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu!")
            return

        if QMessageBox.question(
            self,
            "Konfirmasi",
            "Yakin ingin menghapus data Register CV?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            self.ui.tableRegisterCV.removeRow(row)
            self.reset_form()

    # ================= UTIL =================
    def reset_form(self):
        self.ui.txtNoRegister.clear()
        self.ui.txtNamaCV.clear()
        self.ui.txtModal.clear()
        self.ui.txtNamaPemilik.clear()
        self.ui.txtNamaNotaris.clear()
        self.ui.txtJangkaWaktu.clear()
        self.ui.txtKeterangan.clear()
        self.ui.rbBaru.setChecked(True)
        self.ui.dateRegister.setDate(QDate.currentDate())
        self.ui.dateBerdiri.setDate(QDate.currentDate())
        self.ui.tableRegisterCV.clearSelection()
