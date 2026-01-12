# polymorphism
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return "Hewan bersuara"
    
class Kucing(Hewan):
    def suara(self):
        return f"{self.nama} Miaw"
    
class Anjing(Hewan):
    def suara(self):
        return f"{self.nama} Aug!"
    
class Ayam(Hewan):
    def suara(self):
        return f"{self.nama} Pekok!"

hewan_list = [
    Kucing("Kucing"),
    Anjing("Anjing"),
    Ayam("Ayam")
]

for hewan in hewan_list:
    print(hewan.suara())
# membuat method di kelas orang tua yang diturunkan secara sama di semua
# kelas turunannya, tapi dengan implementasi atau bentuk yang berbeda-beda

print(" ")

# duck typing
class Mobil:
    def nyalakan(self):
        return "Mesin mobil menyala"
    
class Motor:
    def nyalakan(self):
        return "Mesin motor menyala"
    
class Perahu:
    def nyalakan(self):
        return "Mesin perahu menyala"
    
class Pesawat:
    def nyalakan(self):
        return "Mesin pesawat menyala"

# function yang polymorphic  
def nyalakan_kendaraan(kendaraan):
    print(kendaraan.nyalakan())

kendaraan_list = [
    Mobil(),
    Motor(),
    Perahu(),
    Pesawat()
]

for kendaraan in kendaraan_list:
    nyalakan_kendaraan(kendaraan)
# polymorphism mengabaikan apakah kelas-kelas itu dibentuk dari kelas orang tua
# yang sama atau bukan, yang terpenting memiliki method yang sama

print(" ")

# abstract base class atau interface
from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

class Segitiga(Bentuk):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def luas(self):
        return self.alas * self.tinggi / 2 

class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def luas(self):
        return self.radius * 2 * 3.14

bentuk_list = [
    Segitiga(6, 9),
    Lingkaran(9)
]

for bentuk in bentuk_list:
    print(bentuk.luas())
# membuat abstract base class sebagai kelas orang tua dengan abstract method didalamnya
# untuk memaksa kelas turunannya membuat method yang sama

# Program ini mendemonstrasikan penggunaan konsep polymorphism atau banyak bentuk dalam Object Oriented Programming Python.