
from prettytable import PrettyTable

class Login:
    def __init__(self):
        self._email = []
        self._password = []

    def menu(self):
        print("SELAMAT DATANG DI AKSI PENGEMBANGAN DESA TERTINGGAL MAHASISWA SE-INDONESIA\n")
        x = PrettyTable()
        x.field_names = ["No", "Menu"]
        x.add_row(["1", "Tentang Kegiatan"])
        x.add_row(["2", "Benefit dan Fasilitas"])
        x.add_row(["3", "Syarat Peserta"])
        x.add_row(["4", "Timeline Kegiatan"])
        x.add_row(["5", "Pendaftaran"])
        x.add_row(["6", "Pembayaran"])
        x.add_row(["7", "Call Center"])
        x.add_row(["0", "Keluar"])
        print(x)
        print("")

    def penjelasan(self):
        x = PrettyTable()
        x.field_names = ["No", "Penjelasan"]
        x.add_row(["1", "Kegiatan dilakukan di salah satu desa di Kota Surabaya"])
        x.add_row(["2", "Kegiatan dilakukan selama 3 hari"])
        x.add_row(["3", "Fokus kegiatan adalah pengembangan desa dan SDM"])
        x.add_row(["4", "HTM kegiatan adalah 50K"])
        print(x)
        print("")

    def benefit(self):
        x = PrettyTable()
        x.field_names = ["No", "Benefit"]
        x.add_row(["1", "E-sertifikat"])
        x.add_row(["2", "Relasi"])
        x.add_row(["3", "Ilmu yang bermanfaat"])
        x1 = PrettyTable()
        x1.field_names = ["No", "Fasilitas"]
        x1.add_row(["4", "Makan 3x sehari"])
        x1.add_row(["5", "Penginapan"])
        x1.add_row(["6", "Tiket Pulang Pergi"])
        print(x)
        print("")
        print(x1)
        print("")

    def syarat(self):
        x = PrettyTable()
        x.field_names = ["No", "Syarat Peserta"]
        x.add_row(["1", "Merupakan Mahasiswa Aktif Mahasiswa Se-Indonesia"])
        x.add_row(["2", "Sehat jasmani dan rohani"])
        print(x)
        print("")

    def timeline(self):
        x = PrettyTable()
        x.field_names = ["No", "Kegiatan", "Waktu"]
        x.add_row(["1", "Pendaftaran", "3-10 Januari 2024"])
        x.add_row(["2", "Pelaksanaan", "11 Januari 2024"])
        print(x)
        print("")

    def data(self):
        print('LOGIN')
        email = input("Masukkan email anda : ")
        password = input("Masukkan password anda :")
        self._email.append(email)
        self._password.append(password)
        print("")


class daftar(Login):
    def __init__(self):
        super().__init__()
        self.nama = []
        self.umur = []
        self.gender = []
        self.noHp = []
        self.asal = []
        self.universitas = []

    def data(self):
        nama = input("Masukkan nama anda : ")
        umur = input("Masukkan umur anda : ")
        gender = input("Masukkan jenis Kelamin anda : ")
        noHp = input("Masukkan nomer hp anda : ")
        asal = input("Masukkan asal anda : ")
        universitas = input("Masukkan nama universitas anda : ")
        self.nama.append(nama)
        self.umur.append(umur)
        self.gender.append(gender)
        self.noHp.append(noHp)
        self.asal.append(asal)
        self.universitas.append(universitas)
        print("")

    def show(self):
        x = PrettyTable()
        x.field_names = ["No", "Data Diri"]
        x.add_row(["1",f"Nama: {self.nama[0]}"])
        x.add_row(["2",f"Umur: {self.umur[0]}"])
        x.add_row(["3",f"Gender: {self.gender[0]}"])
        x.add_row(["4",f"No HP: {self.noHp[0]}"])
        x.add_row(["5",f"Asal: {self.asal[0]}"])
        x.add_row(["6",f"Universitas: {self.universitas[0]}"])
        print(x)
        print("")


class transaksi(Login):
    def __init__(self):
        super().__init__()
        self.bank = []
        self.norek = None  

    def rekbank(self, option):
        if option == 1:
            self.norek = "12345678"
        elif option == 2:
            self.norek = "0998765543"
        elif option == 3:
            self.norek = "876523627"
        print("Pembayaran Melalui :")
        print("No rekening : " + self.norek)
        print("NB : Registrasi akan hangus jika tidak melakukan pembayaran dalam 1x24 jam")
        print("")

    def daftarBank(self):
        x = PrettyTable()
        x.field_names = ["No", "Daftar Bank"]
        x.add_row(["1", "Bank BRI"])
        x.add_row(["2", "Bank Mandiri"])
        x.add_row(["3", "Dana"])
        print(x)
        option = int(input("Masukkan pilihan pembayaran ada: "))
        self.rekbank(option)
        print("")

    
    def admin(self):
        print(""" Terkait Informasi Hubungi :
              Ani : 0873863727279
              Budi : 08763827298
            """)
        print("")


class statusBayar(transaksi):
    def __init__(self):
        super().__init__()
        self.statusbayar = []
    
    def status(self):
        isi = input("Apakah anda sudah melakukan pembayaran?(sudah/belum)")
        if isi == "sudah":
            self.statusbayar.append(isi)
            print("")
            print(f"Status Bayar : {self.statusbayar[0]}")
            print("NB : Tunjukkan data tersebut kepada nomer yang tertera di call center untuk dimasukkan ke grup whatsaapp peserta")
            print("")
        else: 
            print("Silahkan bayar dulu!!!")
        self.statusbayar.append(isi)
    
    

login_obj = Login()
daftar_obj = daftar()
transaksi_obj = transaksi()
status_obj = statusBayar()

login_obj.data()

while True:
    login_obj.menu()
    option = int(input("Masukkan pilihan anda : "))
    if option == 1:
        login_obj.penjelasan()
    elif option == 2:
        login_obj.benefit()
    elif option == 3:
        login_obj.syarat()
        
    elif option == 4:
        login_obj.timeline()
        
    elif option == 5:
        daftar_obj.data()
      
        daftar_obj.show()
        option1 = input('Apakah data anda benar??(ya/tidak)')
       
        if option1 == "ya":
            transaksi_obj.daftarBank()
            transaksi_obj.rekbank(option)
            status_obj.status()
        elif option1 == "tidak":
            print("Silahkan isi ulang")
    elif option == 6:
        transaksi_obj.daftarBank()
        
    
    elif option == 7:
        transaksi_obj.admin()

      
    elif option == 0:
        print("Terimakasih!!! Kami tunggu partisipasinya")
        break
    else:
        print("Pilihan tidak tersedia!!!")

