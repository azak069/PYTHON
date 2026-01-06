class Mahasiswa:
    nama = ""
    nim = 0
    prodi = ""
    fakultas = ""
    universitas = ""

    def __init__(self, nama, nim, prodi, fakultas, universitas):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.fakultas = fakultas
        self.universitas = universitas
    
    def perkenalan(self):
        print(f"Nama saya {self.nama}, NIM {self.nim}, dari program studi {self.prodi}, fakultas {self.fakultas}, universitas {self.universitas}.")

    def hello(self, nama):
        print(f"Halo {nama}, nama saya {self.nama}, salam kenal!")

    def __str__(self):
        return f"Mahasiswa (nama={self.nama}, nim={self.nim}, prodi={self.prodi}, fakultas={self.fakultas}, universitas={self.universitas})"
    
    def __eq__(self, other):
        return self.nim == other.nim or self.prodi == other.prodi

mahasiswa1 = Mahasiswa("Azak", 25106050124, "Informatika", "Saintek", "UIN")
mahasiswa2 = Mahasiswa("Budi", 25106050125, "Informatika", "Saintek", "UIN")
mahasiswa1.perkenalan()
mahasiswa1.hello("Budi")
print(f"Info {mahasiswa1}")
print(mahasiswa1 == mahasiswa2)

print(" ")
print("-----------------------")
print(" ")

class BankAccount:
    no = ""
    nama = ""
    saldo = 0.0

    def __init__(self, no, nama, saldo):
        if saldo < 0:
            raise ValueError("Saldo awal tidak boleh negatif.")
        self.saldo = saldo
        self.no = no
        self.nama = nama

azak = BankAccount("1234567890", "Azak", 1000000.0)
budi = BankAccount("0987654321", "Budi", 500000.0)

print(f"Rekening {azak.no} atas nama {azak.nama} memiliki saldo sebesar {azak.saldo}.")