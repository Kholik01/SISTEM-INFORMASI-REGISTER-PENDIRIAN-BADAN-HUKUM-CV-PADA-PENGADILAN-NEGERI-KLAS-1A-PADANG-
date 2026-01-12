import sys
import mysql.connector
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class DataRegister(QWidget):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.koneksi_db()
        self.load_data()

        self.ui.btnCari.clicked.connect(self.cari_data)
        self.ui.btnKeluar.clicked.connect(self.close)

    def load_ui(self):
        loader = QUiLoader()
        file = QFile("data_register.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

    def koneksi_db(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hukum"
            )
            self.cursor = self.db.cursor()  # ✅ WAJIB ()
            print("Koneksi database berhasil")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", str(e))

    def load_data(self):
        query = """
            SELECT no_register, kode_cv, nama_cv, alamat_cv,
                   tgl_berdiri, notaris, modal, jangka_berdiri, status
            FROM register_cv
        """
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        table = self.ui.tableRegister
        table.setRowCount(0)

        for r, row in enumerate(rows):
            table.insertRow(r)
            for c, val in enumerate(row):
                table.setItem(r, c, QTableWidgetItem(str(val)))

    def cari_data(self):
        key = self.ui.cmbCari.currentText()
        sql = """
            SELECT no_register, kode_cv, nama_cv, alamat_cv,
                   tgl_berdiri, notaris, modal, jangka_berdiri, status
            FROM register_cv
            WHERE no_register LIKE %s
               OR nama_cv LIKE %s
               OR kode_cv LIKE %s
        """
        like = f"%{key}%"
        self.cursor.execute(sql, (like, like, like))
        self.load_data()
