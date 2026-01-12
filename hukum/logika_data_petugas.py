from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class LogikaDataPetugas(QWidget):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.init_event()

    def load_ui(self):
        loader = QUiLoader()
        file = QFile("data_petugas.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

        self.setWindowTitle("Data Petugas")
        self.resize(900, 600)

    def init_event(self):
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)
        self.ui.btnKeluar.clicked.connect(self.close)
        self.ui.tablePetugas.cellClicked.connect(self.pilih)

    def simpan(self):
        row = self.ui.tablePetugas.rowCount()
        self.ui.tablePetugas.insertRow(row)

        self.ui.tablePetugas.setItem(row, 0, QTableWidgetItem(self.ui.txtId.text()))
        self.ui.tablePetugas.setItem(row, 1, QTableWidgetItem(self.ui.txtNama.text()))
        self.ui.tablePetugas.setItem(row, 2, QTableWidgetItem(self.ui.txtUser.text()))
        self.ui.tablePetugas.setItem(row, 3, QTableWidgetItem(self.ui.txtPass.text()))

        self.bersih()

    def pilih(self, row, col):
        self.ui.txtId.setText(self.ui.tablePetugas.item(row, 0).text())
        self.ui.txtNama.setText(self.ui.tablePetugas.item(row, 1).text())
        self.ui.txtUser.setText(self.ui.tablePetugas.item(row, 2).text())
        self.ui.txtPass.setText(self.ui.tablePetugas.item(row, 3).text())

    def ubah(self):
        row = self.ui.tablePetugas.currentRow()
        if row < 0:
            return

        self.ui.tablePetugas.setItem(row, 0, QTableWidgetItem(self.ui.txtId.text()))
        self.ui.tablePetugas.setItem(row, 1, QTableWidgetItem(self.ui.txtNama.text()))
        self.ui.tablePetugas.setItem(row, 2, QTableWidgetItem(self.ui.txtUser.text()))
        self.ui.tablePetugas.setItem(row, 3, QTableWidgetItem(self.ui.txtPass.text()))

    def hapus(self):
        row = self.ui.tablePetugas.currentRow()
        if row >= 0:
            self.ui.tablePetugas.removeRow(row)
            self.bersih()

    def bersih(self):
        self.ui.txtId.clear()
        self.ui.txtNama.clear()
        self.ui.txtUser.clear()
        self.ui.txtPass.clear()
