import pymysql


class DataBase:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="hukum"
            )
            self.cursor = self.conn.cursor()
            print("Koneksi database berhasil")
        except Exception as e:
            print("Gagal koneksi database:", e)

    # ================= PEMILIK =================
    def ambil_semua_pemilik(self):
        self.cursor.execute("""
            SELECT kd_pemilik, nm_pemilik, jk, alamat, no_tlp
            FROM pemilik
        """)
        return self.cursor.fetchall()

    def tambah_pemilik(self, kd, nama, jk, alamat, telp):
        self.cursor.execute("""
            INSERT INTO pemilik
            (kd_pemilik, nm_pemilik, jk, alamat, no_tlp)
            VALUES (%s,%s,%s,%s,%s)
        """, (kd, nama, jk, alamat, telp))
        self.conn.commit()

    def ubah_pemilik(self, kd, nama, jk, alamat, telp):
        self.cursor.execute("""
            UPDATE pemilik SET
            nm_pemilik=%s,
            jk=%s,
            alamat=%s,
            no_tlp=%s
            WHERE kd_pemilik=%s
        """, (nama, jk, alamat, telp, kd))
        self.conn.commit()

    def hapus_pemilik(self, kd):
        self.cursor.execute(
            "DELETE FROM pemilik WHERE kd_pemilik=%s", (kd,)
        )
        self.conn.commit()

    # ================= NOTARIS =================
    def ambil_semua_notaris(self):
        self.cursor.execute("""
            SELECT kd_notaris, nm_notaris, jk, alamat, no_tlp
            FROM notaris
        """)
        return self.cursor.fetchall()

    def tambah_notaris(self, kd, nama, jk, alamat, telp):
        self.cursor.execute("""
            INSERT INTO notaris
            (kd_notaris, nm_notaris, jk, alamat, no_tlp)
            VALUES (%s,%s,%s,%s,%s)
        """, (kd, nama, jk, alamat, telp))
        self.conn.commit()

    def ubah_notaris(self, kd, nama, jk, alamat, telp):
        self.cursor.execute("""
            UPDATE notaris SET
            nm_notaris=%s,
            jk=%s,
            alamat=%s,
            no_tlp=%s
            WHERE kd_notaris=%s
        """, (nama, jk, alamat, telp, kd))
        self.conn.commit()

    def hapus_notaris(self, kd):
        self.cursor.execute(
            "DELETE FROM notaris WHERE kd_notaris=%s", (kd,)
        )
        self.conn.commit()

    # ================= CV =================
    def ambil_semua_cv(self):
        self.cursor.execute("""
            SELECT kode_cv, nama_cv, alamat_cv, modal, tanggal_berdiri, jenis_usaha
            FROM cv
        """)
        return self.cursor.fetchall()
