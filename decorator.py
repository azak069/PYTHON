class Matematika: # Membuat kelas Matematika

    @staticmethod # method statis untuk menjadikan method tidak tergantung pada instance/objek
    def tambah(a, b):
        return a + b

    @staticmethod
    def kurang(a, b):
        return a - b
    
    @staticmethod
    def kali(a, b):
        return a * b
    
    @staticmethod
    def bagi(a, b):
        if b == 0:
            raise ValueError("Pembagi tidak boleh nol.")
        return a / b

print(Matematika.tambah(10, 5))  # Mengakses method statis tanpa membuat instance/objek  
print(Matematika.kurang(10, 5))
print(Matematika.kali(10, 5))
print(Matematika.bagi(10, 5))

print(" ")
print("-----------------------")
print(" ")

class BankAccount: # Membuat kelas BankAccount
    no = ""
    saldo = 0.0
    active = True

    def __init__(self, no, saldo = 0.0): # method konstruktor
        self.no = no
        self.saldo = saldo
    
    @classmethod # method kelas untuk membuat method yang membuat objek dalam kelas yang sama
    def disabled(cls, no, saldo): # method kelas untuk membuat akun yang non-aktif
       result = cls(no, saldo)
       result.active = False
       return result
    
account1 = BankAccount("1234567890", 1000000.0) # membuat objek account1
account2 = BankAccount.disabled("0987654321", 500000.0) # membuat objek account2 yang non-aktif
print(f"Bank Account 1 - No: {account1.no}, Saldo: {account1.saldo}, Active: {account1.active}") # menampilkan info account1
print(f"Bank Account 2 - No: {account2.no}, Saldo: {account2.saldo}, Active: {account2.active}") # menampilkan info account2

class Category: # Membuat kelas Category
    _nama = "" # atribut yang harus diakses melalui getter dan setter

    @property # getter untuk mendapatkan nilai atribut nama
    def nama(self):
        return self._nama

    @nama.setter # setter untuk mengatur nilai atribut nama dengan validasi
    def nama(self, nama):
        if nama == "":
            raise ValueError("Nama kategori tidak boleh kosong.")
        self._nama = nama   

kategori1 = Category() # membuat objek kategori1
kategori1.nama = "Elektronik" # mengatur nama kategori menggunakan setter
print(kategori1.nama) # menampilkan nama kategori menggunakan getter

# Program ini menunjukkan penggunaan dekorator dalam kelas Python.