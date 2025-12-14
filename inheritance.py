class Hewan: # membuat kelas induk Hewan
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def info(self):
        return f"Hewan ini bernama {self.nama} dan berumur {self.umur} tahun."
    # membuat method info untuk menampilkan informasi hewan yang bisa diwariskan ke kelas turunan

class Kucing(Hewan): # membuat kelas turunan Kucing dari kelas Hewan
    def __init__(self, nama, umur, warna, ras):
        super().__init__(nama, umur) # memanggil pewarisan dari kelas induk
        self.warna = warna
        self.ras = ras

class Anjing(Hewan): # membuat kelas turunan Anjing dari kelas Hewan
    def __init__(self, nama, umur, ukuran, jenis):
        super().__init__(nama, umur) # memanggil pewarisan dari kelas induk
        self.ukuran = ukuran
        self.jenis = jenis

kucing1 = Kucing("Mimi", 2, "Putih", "Persia") # membuat objek kucing1
anjing1 = Anjing("Buddy", 3, "Besar", "Golden Retriever") # membuat objek anjing1
print(kucing1.info()) # memanggil method info dari objek kucing1
print(anjing1.info()) # memanggil method info dari objek anjing1
