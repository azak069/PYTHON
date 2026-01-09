class Category:
    _nama = "" # atribut dengan satu garis bawah untuk enkapsulasi yang ringan
                # hanya memberitahu bahwa ini adalah atribut yang sebaiknya diakses melalui getter dan setter 
                # bukan langsung dari luar kelas
    @property
    def nama(self): # getter untuk mendapatkan nilai atribut nama
        return self._nama

    @nama.setter # setter untuk mengatur nilai atribut nama dengan validasi
    def nama(self, nama):
        if nama == "":
            raise ValueError("Nama kategori tidak boleh kosong.")
        self._nama = nama

kategori1 = Category() # membuat objek kategori1
kategori1.nama = "Digital" # mengatur nama kategori menggunakan setter
print(f"Nama Kategori: {kategori1.nama}")

print(" ")
print("-----------------------")
print(" ")

class BankAccount:
    __no = "" # atribut dengan dua garis bawah untuk enkapsulasi yang lebih ketat
    __saldo = 0.0 # benar- benar hanya bisa diakses melalui getter dan method, tidak bisa langsung dari luar kelas

    def __init__(self, no): # method konstruktor
        self.__no = no

    @property
    def saldo(self): # getter untuk mendapatkan nilai atribut saldo
        return self.__saldo
    
    @property
    def no(self): # getter untuk mendapatkan nilai atribut no
        return self.__no
    
    def topup(self, amount): # method untuk menambah saldo
        if amount <= 0:
            raise ValueError("Jumlah top-up harus positif.")
        self.__saldo += amount
    
    def cashout(self, amount): # method untuk mengurangi saldo
        if amount <= 0:
            raise ValueError("Jumlah cash-out harus positif.")
        if amount > self.__saldo:
            raise ValueError("Saldo tidak mencukupi untuk cash-out.")
        self.__saldo -= amount

zaki = BankAccount("1234567890") # membuat objek zaki
print(f"Nomor Rekening: {zaki.no}") 
print(f"Saldo Awal: {zaki.saldo}")
zaki.topup(500000.0) # menambah saldo
print(f"Saldo setelah top-up: {zaki.saldo}")
zaki.cashout(200000.0) # mengurangi saldo
print(f"Saldo setelah cash-out: {zaki.saldo}")

# Program ini mendemonstrasikan konsep enkapsulasi dalam pemrograman berorientasi objek menggunakan Python untuk melindungi atribut kelas dari akses langsung dari luar kelas.