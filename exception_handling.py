class AkunBank:
    def __init__(self, nomor, saldo=0):
        self.nomor = nomor
        self.saldo = saldo

    def bayar(self, harga):
        if harga > self.saldo:
            raise ValueError("Saldo tidak mencukupi!")
        self.saldo -= harga
# membuat kelas dengan method yang bisa saja mengalami error
# dan jika error, program akan berhenti

try:
    zaki = AkunBank(6699, 50000)
    zaki.bayar(100000)
except ValueError as e:
    print(f"Error : {e}")
# menggunakan try except agar program tidak berhenti dan crash
# walaupun menemui error pada method dalam objek

print(" ")

class SaldoTidakCukup(Exception): # membuat penanganan error spesifik
    def __init__(self, pesan):
        self.pesan = pesan

    def __str__(self):
        return self.pesan
    
class AkunBank2:
    def __init__(self, nomor, saldo=0):
        self.nomor = nomor
        self.saldo = saldo

    def bayar(self, harga):
        if harga > self.saldo:
            raise SaldoTidakCukup("Saldo tidak mencukupi!")
        self.saldo -= harga

try:
    david = AkunBank2(6699, 50000)
    david.bayar(100000)
except SaldoTidakCukup as e:
    print(f"Error : {e}")
# membuat penanganan atau exception error sendiri yang spesifik menggunakan kelas
# agar tidak hanya ValueError semua

# Program ini mendemonstrasikan pencegahan dan penanganan error dalam Object Oriented Programming Python.