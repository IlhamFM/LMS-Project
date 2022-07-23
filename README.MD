## Library Management System

- Tujuan Pengerjaan Project
  Aplikasi ini ditujukan untuk mengakomodir kebutuhan sistem perpustakaan digital sederhana yang dapat membuat dan
  menampilkan daftar dan buku perpustakaan serta dapat melakukan pencarian buku.

- Deskripsi Fungsi
  > main.py
    Fungsi utama aplikasi ada pada file ini, dimana dia mula-mula akan membuat object/instance dari class
    LibraryManagement
    * __init__()
      Konstruktor ini akan membuat koneksi ke SQL dengan membuat objek dari database.py. Setelah session ini terjalin
      maka dia akan memeriksa apakah database lms sudah tersedia pada SQL, jika belum maka fungsi akan membuat databse 
      lms
    * menu()
      setelah pembuatan dan akses database lms, maka fungsi ini akan terus dijalankan sampai mendapatkan input 9. 
      Fungsi ini berisi tampilan menu pada aplikasi
    * user_baru()
      Input 1 pada menu akan memanggil fungsi ini yang kemudian akan membuat tabel user (jika belum ada) lalu akan      
	  menginput data user dengan memanggil fungsi db.eksekusi_query
    * buku_baru()
	  Input 2 akan memanggil fungsi ini yang kemudian akan membuat tabel buku (jika belum ada) lalu akan menginput data 
      buku dengan memanggil fungsi db.eksekusi_query
    * peminjaman()
	  Input 3 akan memanggil fungsi ini yang kemudian akan membuat tabel peminjaman (jika belum ada) lalu akan menginput 
      data peminjaman dan juga memperbarui stok buku dengan memanggil fungsi db.eksekusi_query
    * ambil_data()
	  Fungsi ini dipanggil oleh fungsi tampilkan_data untuk mengambil data-data dari tabel SQL
	* tampilkan_data()
	  Input 4,5 dan 6 dan fungsi cari_data akan memanggil fungsi ini yang digunakan untuk menampilkan (print) data dari
	  tabel dan ditampilkan dalam format data Frame
	* tampilkan_data()
	  Input 7 akan memanggil fungsi ini yang digunakan untuk menampilkan hasil pencarian data pada tabel buku
    * pengembalian()
	  Input 8 akan memanggil fungsi ini yang kemudian akan membuat tabel pengembalian (jika belum ada) lalu akan menginput 
      data pengembalian dan juga memperbarui stok buku dengan memanggil fungsi db.eksekusi_query
  > database.py
    File ini berfungsi untuk membuat database, tabel atau query SQL yang terkait dengan kebutuhan aplikasi
	* __init__()
      Konstruktor ini akan menginisiasi sessaion atau akses ke SQL
	* konek_database()
	  Fungsi ini untuk membuat koneksi atau session pada suatu database di SQL
	* tutup_database()
	  Fungsi ini untuk memutus koneksi atau session dari suatu database di SQL
	  fungsi konek_database dan tutup_database dipanggil di awal dan akhir pilihan menu untuk menghindari adanya error, 
	  khusunya error "Unread result found" walau cursor(buffered=True) telah digunakan pada insiasi koneksi database
	* cek_db_tabel()
	  Fungsi ini untuk memeriksa apakah suatu database atau tabel sudah dibuat/tersedia pada SQL
	* eksekusi_query()
	  Fungsi ini mengeksekusi bermacam jenis query baik itu perintah create, insert, update ataupun delete
	  
- Cara Running program
  > Pada WSL Ubuntu
    python3 main.py 
  > Pada Windows 10
    python main.py

- Test-case

MySQL database connection successfull

-----------LIBRARY MANAGEMENT-----------
  1. Pendaftaran User Baru
  2. Pendaftaran Buku Baru
  3. Peminjaman
  4. Tampilkan Daftar Buku
  5. Tampilkan Daftar User
  6. Tampilkan Daftar Peminjaman
  7. Cari Buku
  8. Pengembalian
  9. Exit
----------------------------------------
Masukkan Nomor Tugas : 4

----------------------------------------------------
  id_buku                    nama_buku kategori_buku  stok_buku
0    0789  Historical Fact And Fiction       Sejarah          2
1    1587                   Statistics    Matematika          3
2    1876        Islam dan Sekulerisme     Pemikiran          3
3    6346                Rencana Besar         Novel          5
4    6840                   Sudut Mati         Novel          3

-----------LIBRARY MANAGEMENT-----------
  1. Pendaftaran User Baru
  2. Pendaftaran Buku Baru
  3. Peminjaman
  4. Tampilkan Daftar Buku
  5. Tampilkan Daftar User
  6. Tampilkan Daftar Peminjaman
  7. Cari Buku
  8. Pengembalian
  9. Exit
----------------------------------------
Masukkan Nomor Tugas : 6

----------------------------------------------------
   id_user user_name id_buku                    nama_buku  tgl_pinjam tgl_pengembalian
0        2     Ujang    6840                   Sudut Mati  2022-07-23       2022-07-26
1        5  Muslimah    0789  Historical Fact And Fiction  2022-07-23       2022-07-26

-----------LIBRARY MANAGEMENT-----------
  1. Pendaftaran User Baru
  2. Pendaftaran Buku Baru
  3. Peminjaman
  4. Tampilkan Daftar Buku
  5. Tampilkan Daftar User
  6. Tampilkan Daftar Peminjaman
  7. Cari Buku
  8. Pengembalian
  9. Exit
----------------------------------------
Masukkan Nomor Tugas : 5

----------------------------------------------------
   id_user user_name   tgl_lahir   pekerjaan         alamat
0        1      Ical  2008-02-29     Pelajar       Sukabaca
1        2     Ujang  2004-01-01   Mahasiswa  Desa Ciherang
2        3      Agus  1998-12-31    Karyawan         Kemang
3        4       Opa  1990-07-16  Wiraswasta  Pondok Indah
4        5  Muslimah  1980-06-10        Guru        Menteng

-----------LIBRARY MANAGEMENT-----------
  1. Pendaftaran User Baru
  2. Pendaftaran Buku Baru
  3. Peminjaman
  4. Tampilkan Daftar Buku
  5. Tampilkan Daftar User
  6. Tampilkan Daftar Peminjaman
  7. Cari Buku
  8. Pengembalian
  9. Exit
----------------------------------------
Masukkan Nomor Tugas : 3

----------------------------------------------------
Masukkan id peminjam : 5
Masukkan id buku : 1876
Masukkan nama peminjam : Muslimah
Masukkan nama buku : Islam dan Sekulerisme
Query berhasil dieksekusi
--------------------------
Data berhasil ditambahkan!
--------------------------
Query berhasil dieksekusi
--------------------------
Buku dipinjamkan ke Muslimah


-----------LIBRARY MANAGEMENT-----------
  1. Pendaftaran User Baru
  2. Pendaftaran Buku Baru
  3. Peminjaman
  4. Tampilkan Daftar Buku
  5. Tampilkan Daftar User
  6. Tampilkan Daftar Peminjaman
  7. Cari Buku
  8. Pengembalian
  9. Exit
----------------------------------------
Masukkan Nomor Tugas : 4

----------------------------------------------------
  id_buku                    nama_buku kategori_buku  stok_buku
0    0789  Historical Fact And Fiction       Sejarah          2
1    1587                   Statistics    Matematika          3
2    1876        Islam dan Sekulerisme     Pemikiran          2
3    6346                Rencana Besar         Novel          5
4    6840                   Sudut Mati         Novel          3

-----------LIBRARY MANAGEMENT-----------
  1. Pendaftaran User Baru
  2. Pendaftaran Buku Baru
  3. Peminjaman
  4. Tampilkan Daftar Buku
  5. Tampilkan Daftar User
  6. Tampilkan Daftar Peminjaman
  7. Cari Buku
  8. Pengembalian
  9. Exit
----------------------------------------
Masukkan Nomor Tugas : 6

----------------------------------------------------
   id_user user_name id_buku                    nama_buku  tgl_pinjam tgl_pengembalian
0        2     Ujang    6840                   Sudut Mati  2022-07-23       2022-07-26
1        5  Muslimah    0789  Historical Fact And Fiction  2022-07-23       2022-07-26
2        5  Muslimah    1876        Islam dan Sekulerisme  2022-07-23       2022-07-26

-----------LIBRARY MANAGEMENT-----------
  1. Pendaftaran User Baru
  2. Pendaftaran Buku Baru
  3. Peminjaman
  4. Tampilkan Daftar Buku
  5. Tampilkan Daftar User
  6. Tampilkan Daftar Peminjaman
  7. Cari Buku
  8. Pengembalian
  9. Exit
----------------------------------------
Masukkan Nomor Tugas : 9

----------------------------------------------------
Sampai Jumpa

- Saran Perbaikan
  Hal-hal yang dapat diperbaiki adalah pada bagian 
  1. defending program untuk format id_buku yang mungkin bisa merujuk pada ISBN
  2. Input pada bagian peminjaman tidak memerlukan input id dan nama, tetapi cukup salah satu 
     dari id (id_buku & id_user) atau nama (nama_buku & user_name)