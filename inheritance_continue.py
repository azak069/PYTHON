# class parent
class Kendaraan: # membuat kelas orang tua

    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun

    def info(self):
        return f"Merek: {self.merek}, Tahun: {self.tahun}"

    def nyalakan(self):
        print(f'{self.merek} dinyalakan.')

# class child
class Mobil(Kendaraan): # membuat kelas anak yang mewarisi sifat dari kelas orang tua

    def __init__(self, merek, tahun, roda): # function super untuk mengakses method yang sama dari kelas orang tua
        super().__init__(merek, tahun)
        self.roda = roda

    def klakson(self): # mengakses method info dari kelas orang tua di kelas anak
        print(f"Mobil {self.info()} dengan jumlah roda {self.roda} memiliki klakson.")

# class child
class Motor(Kendaraan):

    def klakson(self):
        print(f"Motor {self.info()} tidak memiliki klakson")

    def nyalakan(self): # method overriding untuk mengganti method dari kelas orang tua dengan kelas anak
        print(f"Motor {self.merek} dinyalakan otomatis.")

fortuner = Mobil("Fortuner", 2015, 4) # membuat objek dari kelas Mobil yang juga mewarisi sifat dari kelas Kendaraan
fortuner.nyalakan() # mengakses method dari kelas orang tua
fortuner.klakson() # mengakses method pribadi dari kelas anak sendiri

harley = Motor("Harley Davidson", 1995)
harley.nyalakan()
harley.klakson()

# multilevel inheritance atau pewarisan berkali-kali
class Karyawan:

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

class KaryawanTetap(Karyawan):
    pass

class Manager(KaryawanTetap):
    pass

class VicePresident(Manager):
    pass
# kelas KaryawanTetap mewarisi dari kelas Karyawan, kelas Manager mewarisi dari kelas KaryawanTetap, dan seterusnya

# multiple inheritance atau satu kelas anak yang mewarisi dari dua kelas orang tua
class BisaBerenang:
    def berenang(self):
        print("Bisa berenang")

class BisaBerlari:
    def berlari(self):
        print("Bisa Berlari")

class Atlit(BisaBerenang, BisaBerlari):
    def __init__(self, nama):
        self.nama = nama

zaki = Atlit("Zaki")
zaki.berenang()
zaki.berlari()

# diamond problem yang bisa terjadi karena multiple inheritance
class A:
    def method(self):
        return "Method dari A"
    
class B(A):
    def metho(self):
        return "Method dari B"
    
class C(A):
    def method(self):
        return "Method dari C"
    
class D(B, C):
    pass

d = D()
print(d.method())

# type checking dengan isinstance untuk mengecek apakah suatu objek dibuat dari suatu kelas atau turunannya
zaki = Karyawan("Zaki", 10000000)
budi = KaryawanTetap("Budi", 100000000)
david = Manager("David", 1000000000)
jokowi = VicePresident("Jokowi", 10000000000)

print(isinstance(zaki, Karyawan))
print(isinstance(budi, Karyawan))
print(isinstance(david, Karyawan))
print(isinstance(jokowi, Karyawan))

# Program ini mendemonstrasikan penggunaan inheritance atau pewarisan kelas dalam Object Oriented Programming pada Python lebih lanjut.