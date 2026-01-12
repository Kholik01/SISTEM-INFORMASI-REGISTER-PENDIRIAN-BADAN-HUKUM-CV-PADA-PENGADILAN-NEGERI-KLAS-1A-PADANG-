from PySide6.QtWidgets import (
    QWidget, QMessageBox, QComboBox,
    QTableWidget, QTableWidgetItem, QFileDialog
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QPdfWriter, QPainter, QPageSize
from datetime import datetime
import pymysql


class LogikaMenuLaporan(QWidget):
    def __init__(self):
        super().__init__()
        self.db_connect()
        self.load_ui()
        self.init_table()
        self.init_combo()
        self.connect_signal()

    # ================= DATABASE =================
    def db_connect(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="hukum"
        )
        self.cursor = self.conn.cursor()

    # ================= LOAD UI =================
    def load_ui(self):
        loader = QUiLoader()
        file = QFile("menu_laporan.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

        self.table: QTableWidget = self.ui.findChild(QTableWidget, "tableWidget")

    # ================= TABLE =================
    def init_table(self):
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels([
            "No Register",
            "Tanggal",
            "Jenis Laporan",
            "Kode CV",
            "Nama CV",
            "Pemilik",
            "Notaris",
            "Status",
            "Keterangan"
        ])

    # ================= COMBO =================
    def init_combo(self):
        self.bulan_map = {
            "Januari": 1, "Februari": 2, "Maret": 3, "April": 4,
            "Mei": 5, "Juni": 6, "Juli": 7, "Agustus": 8,
            "September": 9, "Oktober": 10, "November": 11, "Desember": 12
        }

        tahun_list = [
            str(y) for y in range(datetime.now().year - 5, datetime.now().year + 1)
        ]

        for name in ["cbBulan", "cbBulan2", "cbBulan3"]:
            cb = self.ui.findChild(QComboBox, name)
            if cb:
                cb.clear()
                cb.addItems(self.bulan_map.keys())

        for name in ["cbTahun", "cbTahun2", "cbTahun3"]:
            cb = self.ui.findChild(QComboBox, name)
            if cb:
                cb.clear()
                cb.addItems(tahun_list)

    # ================= SIGNAL =================
    def connect_signal(self):
        self.ui.btnCetakCV.clicked.connect(self.load_keseluruhan)
        self.ui.btnLihatTahun.clicked.connect(self.load_pertahun)
        self.ui.btnCetakStatus.clicked.connect(self.cetak_pdf)

    # ================= DATA =================
    def isi_table(self, data):
        self.table.setRowCount(0)
        for row_data in data:
            row = self.table.rowCount()
            self.table.insertRow(row)
            for col, val in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(str(val)))

    def load_keseluruhan(self):
        self.cursor.execute("""
            SELECT no_register, tgl_register, jenis_laporan,
                   kode_cv, nama_cv, nama_pemilik,
                   nama_notaris, status_register, keterangan
            FROM menu_laporan
        """)
        self.isi_table(self.cursor.fetchall())

    def load_pertahun(self):
        tahun = self.ui.cbTahun3.currentText()
        self.cursor.execute("""
            SELECT no_register, tgl_register, jenis_laporan,
                   kode_cv, nama_cv, nama_pemilik,
                   nama_notaris, status_register, keterangan
            FROM menu_laporan
            WHERE YEAR(tgl_register) = %s
        """, (tahun,))
        self.isi_table(self.cursor.fetchall())

    # ================= CETAK PDF (TABEL RAPI) =================
    def cetak_pdf(self):
        if self.table.rowCount() == 0:
            QMessageBox.warning(self, "Peringatan", "Tidak ada data untuk dicetak")
            return

        path, _ = QFileDialog.getSaveFileName(
            self,
            "Simpan PDF",
            "laporan_status_cv.pdf",
            "PDF Files (*.pdf)"
        )
        if not path:
            return

        pdf = QPdfWriter(path)
        pdf.setResolution(300)
        pdf.setPageSize(QPageSize(QPageSize.A4))

        painter = QPainter(pdf)
        painter.setFont(self.font())

        # ===== KONFIGURASI TABEL =====
        margin_x = 40
        margin_y = 80
        row_height = 32

        # Lebar kolom (TOTAL ≈ A4)
        col_widths = [80, 90, 90, 70, 120, 120, 120, 80, 150]

        page_width = pdf.width() - margin_x * 2
        y = margin_y

        # ===== JUDUL =====
        painter.drawText(
            margin_x,
            40,
            page_width,
            30,
            Qt.AlignCenter,
            "LAPORAN STATUS CV"
        )

        # ===== HEADER =====
        x = margin_x
        for col, width in enumerate(col_widths):
            painter.drawRect(x, y, width, row_height)
            painter.drawText(
                x + 5, y + 5,
                width - 10, row_height - 10,
                Qt.AlignCenter | Qt.TextWordWrap,
                self.table.horizontalHeaderItem(col).text()
            )
            x += width
        y += row_height

        # ===== DATA =====
        for row in range(self.table.rowCount()):
            if y + row_height > pdf.height() - margin_y:
                pdf.newPage()
                y = margin_y

            x = margin_x
            for col, width in enumerate(col_widths):
                painter.drawRect(x, y, width, row_height)
                item = self.table.item(row, col)
                text = item.text() if item else ""
                painter.drawText(
                    x + 5, y + 5,
                    width - 10, row_height - 10,
                    Qt.AlignLeft | Qt.AlignVCenter | Qt.TextWordWrap,
                    text
                )
                x += width
            y += row_height

        painter.end()
        QMessageBox.information(self, "Sukses", "PDF berhasil disimpan dengan format tabel")


MenuLaporan = LogikaMenuLaporan
