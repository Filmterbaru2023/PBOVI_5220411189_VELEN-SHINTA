class katalog:
    def __init__(self):
        pass
    
    def cari(self):
        pass

class Perpusltem:
    def __init__(self,judul,subjek):
        self.judul = judul
        self.subjek = subjek

    def LokasiPenyimpan(self):
        return self.subjek

    def info(self):
        return self.judul

class buku(Perpusltem):
    def __init__(self,judul,subjek,isbn,pengarang,jmlhal,ukuran):
        super().__init__(judul,subjek)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal
        self.ukuran = ukuran

class pengarang:
    def __init__(self,a):
        self.nama = a

    def info(self):
        return self.nama

    def cari(self):
        return self.nama

class majalah(Perpusltem):
    def __init__(self,judul,subjek,volume,issue):
        super().__init__(judul,subjek)
        self.volume = volume
        self.issue = issue

class DVD(Perpusltem):
    def __init__(self,judul,subjek,aktor,genre):
        super().__init__(judul,subjek)
        self.aktor = aktor
        self.genre = genre

