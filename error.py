# Macam-macam jenis error di Python:
# SyntaxError untuk kesalahan sintaks
# NameError untuk variabel yang tidak didefinisikan
# ValueError untuk tipe data yang tidak sesuai
# TypeError untuk operasi dengan tipe data yang tidak sesuai
# IndexError untuk indeks di luar jangkauan
# KeyError untuk kunci yang tidak ada dalam dictionary
# ZeroDivisionError untuk pembagian dengan nol
print("=== KALKULATOR SEDERHANA ===")
# try digunakan untuk menangani error yang mungkin terjadi
# except digunakan untuk menangani error tertentu
try:
    a = int(input("Angka Pertama : "))
    b = int(input("Angka Kedua : "))
    hasil = a / b
    print(f"Hasil : {hasil}")
except ValueError:
    print("Tolong masukkan angka!") # menangani kesalahan jika input bukan angka
except TypeError:
    print("Tolong masukkan angka!") # menangani kesalahan tipe data
except ZeroDivisionError:
    print("Tidak bisa dibagi nol!") # menangani kesalahan pembagian dengan nol
except:
    print("Terjadi Kesalahan!") # menangani kesalahan umum

print("=== PROGRAM SELESAI! ===")

try:
    a = int(input("Masukkan angka : "))
except ValueError:
    print("Tolong masukkan angka!") # menangani kesalahan jika input bukan angka
else:
    print(f"Angka yang Anda masukkan : {a}")
    if a > 0:
        print("Angka positif")
    elif a < 0:
        print("Angka negatif")
    else:
        print("Angka nol")
finally:
    print("Program Selesai!") # finally akan selalu dieksekusi setelah try-except walau ada error atau tidak

# Program ini mendemonstrasikan berbagai jenis penanganan error di Python.