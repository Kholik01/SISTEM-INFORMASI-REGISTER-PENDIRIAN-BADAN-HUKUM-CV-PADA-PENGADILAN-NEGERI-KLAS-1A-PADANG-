import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_form import Ui_main
from logika_data_pemilik import LogikaDataPemilik
from logika_data_notaris import LogikaDataNotaris
from logika_data_cv import DataCV

import logika_data_petugas
import logika_data_register
import logika_data_register_cv
import logika_menu_laporan


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_main()
        self.ui.setupUi(self)

        self.setWindowTitle("Aplikasi Sistem Informasi")
        self.resize(1100, 720)

        # CONNECT MENU
        self.ui.actionData_Pemilik.triggered.connect(self.buka_pemilik)
        self.ui.actionData_Notaris.triggered.connect(self.buka_notaris)
        self.ui.actionData_CV_2.triggered.connect(self.buka_cv)
        self.ui.actionData_Petugas.triggered.connect(self.buka_petugas)
        self.ui.actionData_Register.triggered.connect(self.buka_register)
        self.ui.actionData_Register_CV.triggered.connect(self.buka_register_cv)
        self.ui.actionMenu_Laporan.triggered.connect(self.buka_laporan)

        # SIMPAN FORM YANG SUDAH DIBUKA
        self.form = {}

    # =================================================
    # FORM MANAGER (INI KUNCI)
    # =================================================
    def show_form(self, key, creator):
        if key not in self.form or not self.form[key].isVisible():
            self.form[key] = creator()
        self.form[key].show()
        self.form[key].raise_()
        self.form[key].activateWindow()

    # =================================================
    # MENU ACTION
    # =================================================
    def buka_pemilik(self):
        self.show_form("pemilik", LogikaDataPemilik)

    def buka_notaris(self):
        self.show_form("notaris", LogikaDataNotaris)

    def buka_cv(self):
        self.show_form("cv", DataCV)

    def buka_petugas(self):
        self.show_form("petugas", logika_data_petugas.LogikaDataPetugas)

    def buka_register(self):
        self.show_form("register", logika_data_register.DataRegister)

    def buka_register_cv(self):
        self.show_form("register_cv", logika_data_register_cv.DataRegisterCV)

    def buka_laporan(self):
        self.show_form("laporan", logika_menu_laporan.MenuLaporan)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec())
