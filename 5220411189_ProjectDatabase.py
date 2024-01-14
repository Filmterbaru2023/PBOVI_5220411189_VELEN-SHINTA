import matplotlib.pyplot as plt
import mysql.connector

def koneksi():
    db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "5220411189"
	)
    cursor = db.cursor()
    return db, cursor

class admin:
    def __init__(self):
        self.email = ''
        self.password = ''

    def menuPengguna(self):
        print("=============================")
        print("======= Menu Pengguna =======")
        print("============================= \n")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar\n")

    def login(self):
        print("Silahkan login terlebih dahulu\n")
        self.email = input("Masukkan email khusus admin : ")
        self.password  = input("Masukkan password : ")
        if self.email == "admin123@gmail.com" and self.password == "admin321":
            print("Anda berhasil login\n")
            while True:
                admin().menu()
                optionAdmin = int(input("Masukkan pilihan anda(dalam bentuk angka) : "))
                if optionAdmin == 1:
                    menuDatabase().hapusData()
                    print("Data berhasil dihapus!\n")
                elif optionAdmin == 2:
                    menuDatabase().showTampilSemua()
                elif optionAdmin == 3:
                    menuDatabase().cariData()
                elif optionAdmin == 4:
                    break
                else:
                    print("Pilihan anda tidak tersedia!\n")
        else:
            print("Anda gagal login,silahkan login kembali\n")

    def menu(self):
        print("==============================")
        print("========= Menu Admin =========")
        print("==============================\n")
        print("1. Hapus Data Pengunjung")
        print("2. Tampil data pengunjung")
        print("3. Cari data pengunjung")
        print("4. Keluar\n")

# nomer hp pengunjung sebagai unique key(kunci kedua)
class pengunjung(admin):
    def __init__(self):
        super().__init__()

    def login(self):
        self.email = input("Masukkan email : ")
        self.password = input("Masukkan password : ")
        db, cursor = koneksi()
        sql = "SELECT * FROM login WHERE email=%s and password=%s"
        data = [self.email,self.password]
        cursor.execute(sql,data)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            print("Email sudah terdaftar!\n")
        else:
            print("Email belum terdaftar!")
            print("Silahkan daftarkan email anda terlebih dahulu!")
            self.email = input("Masukkan email : ")
            self.password = input("Masukkan password : ")
            data2 = [self.email,self.password]
            sql = "INSERT INTO login (email,password) VALUES (%s, %s)"
            cursor.execute(sql, data2)
            db.commit()
            print("Email berhasil terdaftar!\n")
        return result
    
    def menu(self):
        print("=========================================")
        print("============ Menu Pengunjung ============")
        print("=========================================\n")
        print("1. Lihat kepadatan pengunjung")
        print("2. Lihat daftar harga tiket")
        print("3. Beli tiket")
        print("4. Keluar\n")

    def hargaTiket(self):
        print("====================================") 
        print("======== Daftar Harga Tiket ========")
        print("====================================\n")
        print("==============")
        print("|   Weekday  |")
        print("==============\n")
        print("1. Dewasa            : Rp 80.000")
        print("2. Anak (0-10 tahun) : Rp 60.000\n")
        print("==============")
        print("|   Weekend  |")
        print("==============\n")
        print("1. Dewasa            : Rp 100.000")
        print("2. Anak (0-10 tahun) : Rp 80.000\n")

class menuDatabase(admin):
    def __init__(self):
        super().__init__()
        self.noHP = ''
        self.nama = ''
        self.dewasa = 0
        self.anak = 0
        self.hari = ''
        self.tanggal = ''

    
    def tambahData(self):
        self.noHP = input("Masukkan No.HP : ")
        self.nama = input("Masukkan nama pemesan : ")
        self.dewasa = int(input("Masukkan kategori dewasa : "))
        self.anak = int(input("Masukkan kategori anak - anak : "))
        self.hari = input("Masukkan hari berkunjung: ")
        self.tanggal = input("Masukkan tanggal berkunjung(00-00-00): ")
        if self.hari=='minggu':
            self.harga = (self.dewasa * 100000) + (self.anak * 80000)
        else:
            self.harga = (self.dewasa * 80000) + (self.anak * 60000)
        data = [self.noHP,self.nama,self.dewasa,self.anak,self.hari,self.tanggal,self.harga]
        db, cursor = koneksi()
        sql = "INSERT INTO wisatawan (noHP,nama,dewasa,anakAnak,hari,tanggal,hargaTiket) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,data)
        db.commit()
    
    def tampilSemua(self):
        db, cursor = koneksi()
        sql = "SELECT nama,dewasa,anakAnak,hari,tanggal,hargaTiket FROM wisatawan"    
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def showTampilSemua(self):
        result = self.tampilSemua()
        for i in result:
            print("======================================")
            print("========= Data Pengunjung ============")
            print("======================================\n")
            print("Nama Pemesan           : ", i[0])
            print("Jumlah tiket dewasa    : ", i[1])
            print("Jumlah tiket anak-anak : ", i[2])
            print("Hari berkunjung        : ", i[3])
            print("Tanggal berkunjung     : ", i[4])
            print("Total harga tiket      : ", i[5])
            print("=======================================\n")
            print()

    def ubahData(self):
        self.noHp = input("Masukkan nomer HP anda: ")
        self.nama = input("Masukkan nama pemesan : ")
        self.dewasa = int(input("Masukkan kategori dewasa : "))
        self.anak = int(input("Masukkan kategori anak - anak : "))
        self.hari = input("Masukkan hari berkunjung: ")
        self.tanggal = input("Masukkan tanggal berkunjung(00-00-00): ")
        if self.hari=='minggu':
            self.harga = (self.dewasa * 100000) + (self.anak * 80000)
        else:
            self.harga = (self.dewasa * 80000) + (self.anak * 60000)
        db, cursor = koneksi()
        data=[self.nama,self.dewasa,self.anak,self.hari,self.tanggal,self.harga,self.noHp]
        sql = "UPDATE wisatawan SET nama=%s,dewasa=%s,anakAnak=%s,hari=%s,tanggal=%s,hargaTiket=%s WHERE noHP=%s"
        cursor.execute(sql,data)
        print("Data berhasil diubah!\n")
        db.commit()

    def tampildata(self):
        self.noHP = input("Masukkan nomer hp anda: ")
        data=[self.noHP]
        db,cursor = koneksi()
        sql = "SELECT nama,dewasa,anakAnak,hari,tanggal,hargaTiket FROM wisatawan WHERE noHP =%s"
        cursor.execute(sql, data)
        result = cursor.fetchall()
        return result
    
    def cariData(self):
        result = self.tampildata()
        for i in result:
            print("=======================================")
            print("============ TIKET WISATA =============")
            print("=======================================\n")
            print("Nama Pemesan           : ", i[0])
            print("Jumlah tiket dewasa    : ", i[1])
            print("Jumlah tiket anak-anak : ", i[2])
            print("Hari berkunjung        : ", i[3])
            print("Tanggal berkunjung     : ", i[4])
            print("Total harga tiket      : ", i[5])
            print("=======================================\n")

    def hapusData(self):
        self.noHP = input("Masukkan No HP anda : ")
        data = [self.noHP]
        db, cursor = koneksi()
        sql = "DELETE FROM wisatawan WHERE noHP=%s"
        cursor.execute(sql, data)
        db.commit()
        print("Data anda berhasil dihapus!\n")

    def hapusAllData(self):
        db, cursor = koneksi()
        sql = "DELETE FROM wisatawan"
        cursor.execute(sql)
        db.commit()
        print("Data berhasil dihapus!")

    def grafik(self):
        db, cursor = koneksi()
        sql = "SELECT COUNT(nama),hari FROM wisatawan GROUP BY hari"
        cursor.execute(sql)
        result = cursor.fetchall()
        data =[]
        for j in result:
            data.append(j[0])
        nama_hari = []
        for j in result:
            nama_hari.append(j[1])
        plt.title("Data Kepadatan Pengunjung")
        plt.xlabel("Hari")
        plt.bar(nama_hari,data)
        plt.show()


print("=========================================")
print("=== SELAMAT DATANG DI WAHANA KELUARGA ===")
print("=========================================\n")
while True:
    admin().menuPengguna()
    option = int(input("Masukkan pilihan anda(dalam bentuk angka): "))
    if option == 1:
        while True:
            admin().login()
    elif option == 2:
        pengunjung().login()
        while True:
            pengunjung().menu()
            option1= int(input("Masukkan pilihan anda(dalam bentuk angka) : "))
            if option1 == 1:
                menuDatabase().grafik()  
            elif option1 == 2:
                pengunjung().hargaTiket()
            elif option1 == 3:
                menuDatabase().tambahData()
                while True:
                    option2 = input("Apakah data sudah benar? (ya/tidak): ")
                    if option2=="ya":
                        menuDatabase().cariData()
                        print("Nomer VA : 0987654231")
                        print("Nomer VA berlaku 1x24 jam")
                        print("Silahkan lakukan pembayaran sesuai dengan total harga tiket")
                        print("Tiket akan berlaku secara otomatis setelah melakukan pembayaran\n")
                        break
                    elif option2=="tidak":
                        print("Lakukan ubah data untuk mengisi ulang\n")
                        menuDatabase().ubahData()
            elif option1==4:
                break
            else:
                print("Pilihan anda tidak tersedia!\n")
    elif option == 3:
        print("Terimakasih, Semoga harimu Menyenangkan!!!")
        break
    else:
        print("Pilihan anda tidak tersedia!\n")




    
