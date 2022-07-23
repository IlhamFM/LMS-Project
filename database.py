import mysql.connector
import pandas as pd

class BuatSQL:
    def __init__(self, user, passwd):
        #fungsi untuk menginisiasi koneksi ke SQL (tanpa koneksi ke sebuah database)
        self.user = user
        self.passwd = passwd
        try:
            self.mydb = mysql.connector.connect(
                host = "localhost",
                user = self.user,
                password = self.passwd)
            # buffered dibuat True untuk menghindari error "Unread result found" saat melakkukan query
            # khususnya setelah query membaca data
            self.mycursor = self.mydb.cursor(buffered=True)
            self.akses = True
            print("MySQL database connection successfull")
        except mysql.connector.Error as err:
            print("Ada kesalahan pada akses MySQL!\n {}".format(err))
            self.akses = False
            
    def konek_database(self, user, passwd, db):
        #fungsi ini digunakan untuk membuat ke sebuah databse yang telah terbuat pada SQL
        self.user = user
        self.passwd = passwd
        try:
            self.mydb = mysql.connector.connect(
                host = "localhost",
                user = self.user,
                password = self.passwd,
                database = db)
            # buffered dibuat True untuk menghindari error "Unread result found" saat melakkukan query
            # khususnya setelah query membaca data
            self.mycursor = self.mydb.cursor(buffered=True)
            self.akses = True
        except mysql.connector.Error as err:
            print("Ada kesalahan pada akses database!\n {}".format(err))
            self.akses = False

    def tutup_database(self):
        # fungsi untuk menutup session database
        self.mycursor.close()
        self.mydb.close()
        
    def cek_db_tabel(self, db_tabel, data):
        #fungsi ini digunakan untuk memeriksa apakah suatu database atau tabel sudah tersedia (True) atau belum (False)
        hasil = False
        self.mycursor.execute("show " + db_tabel)
        for tabel in self.mycursor:
            if data in tabel:
                hasil = True
                break;
            else:
                hasil = False
        return hasil
            
    def eksekusi_query(self, query, perbarui_data = False, value ="", liat_data = False):
        #fungsi ini digunakan untuk mengeksekusi segala jenis query pada SQL
        self.mycursor = self.mydb.cursor()
        try:
            # Blok untuk queri perbaruan data (insert, update, delete)
            if perbarui_data:
                self.mycursor.execute(query, value)
                self.mydb.commit()
                print("Query berhasil dieksekusi")
                # Informasi tambahan untuk query insert
                if len(value)>1 :
                    print("--------------------------")
                    print("Data berhasil ditambahkan!")
                    print("--------------------------")
            # Blok untuk queri melihat data (select, describe)
            elif liat_data:
                self.mycursor.execute(query)
                hasil = self.mycursor.fetchall()
                return hasil
            # Blok untuk queri membuat table atau database (create)
            else:
                self.mycursor.execute(query)
        except mysql.connector.Error as err:
            print("Ada permasalahan pada query SQL\n {}".format(err))
            self.tutup_database()
            
