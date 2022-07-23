import database
from datetime import date, timedelta
import pandas as pd

class LibraryManagement:
    def __init__(self):
        # fungsi ini dimulai dengan menginisiasi koneksi ke SQL
        self.akun = "ds"
        self.passwd = "tgs.pacmann"
        self.database = "lms"
        self.db = database.BuatSQL(self.akun, self.passwd) 
        # kondisional ini digunakan untuk memeriksa apakah database lms yang digunakan sudah tersedia pada sql
        if not self.db.cek_db_tabel("databases", self.database):
             self.db.eksekusi_query("create database lms")
        self.db.tutup_database()
    
    def user_baru(self):
        # Fungsi untuk membuat sekaligus menginput data pada tabel user
        self.db.konek_database(self.akun, self.passwd, self.database)
        nama = input("Masukkan nama user : ")
        tanggal_lahir = input("Masukkan tanggal lahir(YYYY-MM-DD) : ")
        pekerjaan = input("Pekerjaan : ")
        alamat = input("Masukkan alamat : ")
        value = (nama, tanggal_lahir, pekerjaan, alamat)
        
        # blok kondisional untuk memeriksa apakah tabel user sudah tersedia pada SQL
        # Jika belum maka tabel user akan d buat pada blok ini
        if not self.db.cek_db_tabel("tables", "user"):
            self.db.eksekusi_query("""create table user (
                id_user int auto_increment primary key, 
                user_name varchar(100),
                tgl_lahir date, 
                pekerjaan varchar(100),
                alamat varchar(255))""")
        sql = "INSERT INTO user (user_name, tgl_lahir, pekerjaan, alamat) VALUES (%s, %s, %s, %s)"
        self.db.eksekusi_query(sql, True, value)
        self.db.tutup_database()
       
    def buku_baru(self):
        # Fungsi untuk membuat sekaligus menginput data pada tabel buku
        self.db.konek_database(self.akun, self.passwd, self.database)
        kode_buku = input("Masukkan kode buku : ")
        nama_buku = input("Masukkan nama buku : ")
        kategori_buku = input("Masukkan kategori buku : ")
        stok_buku = input("Stok buku : ")
        value = (kode_buku, nama_buku, kategori_buku, stok_buku)
        
        # blok kondisional untuk memeriksa apakah tabel buku sudah tersedia pada SQL
        # Jika belum maka tabel buku akan d buat pada blok ini
        if not self.db.cek_db_tabel("tables", "buku"):
            self.db.eksekusi_query("""create table buku (
                id_buku varchar(30) primary key, 
                nama_buku varchar(50),
                kategori_buku varchar(30),
                stok_buku int)""")
        sql = "INSERT INTO buku (id_buku, nama_buku, kategori_buku, stok_buku) VALUES (%s, %s, %s, %s)"
        self.db.eksekusi_query(sql, True, value)
        self.db.tutup_database()
        
    def peminjaman(self):
        # Fungsi untuk memproses peminjaman buku
        self.db.konek_database(self.akun, self.passwd, self.database)
        id_peminjam = input("Masukkan id peminjam : ")
        id_buku = input("Masukkan id buku : ")
        nama_peminjam = input("Masukkan nama peminjam : ")
        nama_buku = input("Masukkan nama buku : ")
        hr_peminjaman = date.today()
        hr_pengembalian = hr_peminjaman + timedelta(days=3)
        value = (id_peminjam, nama_peminjam, id_buku, nama_buku, hr_peminjaman, hr_pengembalian)
        
        # blok kondisional untuk memeriksa apakah tabel peminjaman sudah tersedia pada SQL
        # Jika belum maka tabel peminjaman akan d buat pada blok ini
        if not self.db.cek_db_tabel("tables", "peminjaman"):
            self.db.eksekusi_query("""create table peminjaman (
                id_user int, 
                user_name varchar(100),
                id_buku varchar(30), 
                nama_buku varchar(50),
                tgl_pinjam date,
				tgl_pengembalian date,
				foreign key (id_user) references user(id_user),
				foreign key (id_buku) references buku(id_buku))""")
        sql = """INSERT INTO peminjaman (id_user, user_name, id_buku, nama_buku, tgl_pinjam,tgl_pengembalian) 
            VALUES (%s, %s, %s, %s, %s, %s)"""
        self.db.eksekusi_query(sql, True, value)
        data_buku = self.ambil_data("buku", " where id_buku = " +  id_buku)
        data_stok = data_buku[0][3]
        # sintaks untuk perbarui data stok pada tabel buku
        update_stok = "update buku set stok_buku = " + str(data_stok-1) + " where id_buku = " + id_buku
        self.db.eksekusi_query(update_stok, True)
        print("--------------------------")
        print("Buku dipinjamkan ke " + nama_peminjam)
        self.db.tutup_database()
        
    def ambil_data(self, db_tabel, where = ""):
        # fungsi untuk mengabmil data atau nama kolom pasa suatu tabel
        data = self.db.eksekusi_query("select * from " + db_tabel + where, liat_data=True)
        return data
    
    def tampilkan_data(self, db_tabel, query = ""):
        # fungsi untuk menampilkan tabel pada suatu database dengan format dataframe
        self.db.konek_database(self.akun, self.passwd, self.database)
        deskripsi_tabel = self.db.eksekusi_query("describe " + db_tabel, liat_data = True)
        nama_kolom = [deskripsi[0] for deskripsi in deskripsi_tabel]
        data_tabel = self.ambil_data(db_tabel, query)
        tabel_data = pd.DataFrame(data=data_tabel, columns=nama_kolom)
        print(tabel_data)
        self.db.tutup_database()
        
    def cari_buku(self, tabel_db):
        # fungsi untuk mendapatkan data buku yang dicari
        nama_buku = input("Masukkan nama buku : ")
        self.tampilkan_data("buku", " where nama_buku like \"%" + nama_buku +"%\"")
        
    def pengembalian(self):
        # fungsi untuk memproses pemngembalian buku
        self.db.konek_database(self.akun, self.passwd, self.database)
        id_peminjam = input("Masukkan id peminjam : ")
        id_buku = input("Masukkan id buku : ")
        query_delete = "delete from peminjaman where id_user = " + str(id_peminjam) + " and id_buku = " + str(id_buku)
        self.db.eksekusi_query(query_delete, True)
        data_buku = self.ambil_data("buku", " where id_buku = " +  id_buku)
        data_stok = data_buku[0][3]
        # sintaks untuk perbarui data stok pada tabel buku
        update_stok = "update buku set stok_buku = " + str(data_stok+1) + " where id_buku = " + id_buku
        self.db.eksekusi_query(update_stok, True)
        print("--------------------------")
        print("Buku telah dikembalikan ")
        self.db.mycursor = self.db.mydb.cursor(buffered=True)
        self.db.tutup_database()
        
    def menu(self):
        # fungsi untuk menampilkan menu Library Management System
        # Menu ini akan ditampilkan terus sampai dimasukkan angka 9
        print("\n-----------LIBRARY MANAGEMENT-----------")
        print("  1. Pendaftaran User Baru")
        print("  2. Pendaftaran Buku Baru")
        print("  3. Peminjaman")
        print("  4. Tampilkan Daftar Buku")
        print("  5. Tampilkan Daftar User")
        print("  6. Tampilkan Daftar Peminjaman")
        print("  7. Cari Buku")
        print("  8. Pengembalian")
        print("  9. Exit")
        print("----------------------------------------")
        pilihan =  input("Masukkan Nomor Tugas : ")
        print("\n----------------------------------------------------")
        try:
            pilihan = int(pilihan)
            if pilihan == 1:
                self.user_baru()
                print()
                self.menu()
            elif pilihan == 2:
                self.buku_baru()
                print()
                self.menu()
            elif pilihan == 3:
                self.peminjaman()
                print()
                self.menu()
            elif pilihan == 4:
                self.tampilkan_data("buku")
                self.menu()
            elif pilihan == 5:
                self.tampilkan_data("user")
                self.menu()
            elif pilihan == 6:
                self.tampilkan_data("peminjaman")
                self.menu()
            elif pilihan == 7:
                self.cari_buku("buku")
                self.menu()
            elif pilihan == 8:
                self.pengembalian()
                print()
                self.menu()
            elif pilihan == 9:
                print("Sampai Jumpa")
            else:
                print("\nINPUT TIDAK SESUAI DENGAN PILIHAN YANG ADA!\n")
                self.menu()
        except ValueError:
            print("\nINPUT YANG ANDA MASUKKAN BUKAN BILANGAN!\n")
            self.menu()
        except Exception as err:
            print("\nADA KESALAHAN PADA PROSES\n {}".format(err))
            self.menu()
              
lm = LibraryManagement()
if (lm.db.akses):
    lm.menu()
    
