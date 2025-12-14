# macam-macam mode file di Python
# r = Baca
# w = Tulis
# a = Tambah
# x = Buat baru

print("== Simpan Data Nilai ==")
file = open("contoh.txt", "w")
# open digunakan untuk membuka file dengan mode tertentu
while True:
    nama = input("Masukkan Nama Siswa : ")
    if nama == "":
        break
    
    nilai = input("Masukkan Nilai Siswa : ")
    
    file.write(f"Nama : {nama}, Nilai : {nilai} \n") # menulis data ke file
    print(f"Data {nama} berhasil ditambahkan!")
    print("Tekan Enter tanpa input untuk selesai!")

file.close() # menutup file setelah selesai digunakan
print("== Program Selesai ==")

# Menginput dan Menyimpan Data ke File

print("== Menampilkan Data Nilai ==")
try:
    with open("contoh.txt", "r") as file: # membuka file dalam mode baca
    # menggunakan with untuk memastikan file ditutup otomatis setelah selesai digunakan
        for line in file:
            data = line.strip().split(",") # memisahkan data berdasarkan koma
            print(f"{data[0]} : {data[1]}") # menampilkan data dari file
except FileNotFoundError:
    print("File tidak ditemukan.") # menangani error jika file tidak ditemukan

print("== Program Selesai ==")

# Membaca dan Menampilkan Data dari File

# Program ini mendemonstrasikan penggunaan operasi file di Python.