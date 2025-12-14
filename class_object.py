class Orang: # mendefinisikan kelas bernama Orang
    nama = "Zaki"
    umur = 20
    pekerjaan = "Programmer"
    
object_orang = Orang() # membuat objek dari kelas Orang
print(type(object_orang)) # menampilkan tipe objek
print(object_orang.nama) # mengakses atribut nama dari objek

object_orang2 = Orang() # membuat objek kedua dari kelas Orang
object_orang2.nama = "Budi" # mengubah atribut nama pada objek kedua
print(object_orang2.nama) # menampilkan atribut nama dari objek kedua
print(object_orang.nama) # menampilkan atribut nama dari objek pertama untuk menunjukkan bahwa nilainya tidak berubah

class Manusia: # mendefinisikan kelas bernama Manusia
    def __init__(self, nama, umur): # membuat method konstruktor untuk inisialisasi atribut
        self.nama = nama
        self.umur = umur

object_manusia = Manusia("Siti", 25) # membuat objek dari kelas Manusia dengan parameter
print(object_manusia.nama) # mengakses atribut nama dari objek
print(object_manusia.__dict__) # menampilkan semua atribut dan nilainya dalam bentuk dictionary

class Saya: # mendefinisikan kelas bernama Saya
    def __init__(self, nama, umur): # membuat method konstruktor untuk inisialisasi atribut
        self.nama = nama
        self.umur = umur

    def sapa(self): # membuat method untuk menyapa
        print(f"Halo, nama saya {self.nama} dan saya berumur {self.umur} tahun.")

object_saya = Saya("Andi", 30) # membuat objek dari kelas Saya dengan parameter
object_saya.sapa() # memanggil method sapa dari objek
object_saya2 = Saya("Rina", 28) # membuat objek kedua dari kelas Saya dengan parameter
object_saya2.sapa() # memanggil method sapa dari objek kedua