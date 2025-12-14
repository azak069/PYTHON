secret = 8

while True:
    tebak = int(input("Tebak angka antara 1 sampai 10: "))

    if tebak == secret:
        print("Selamat! Tebakan Anda benar.")
        break
    else:
        print("Tebakan Anda salah. Coba lagi.")
        continue

# break digunakan untuk keluar dari loop ketika tebakan benar

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"Angka ganjil : {i}")

# continue digunakan untuk melewati iterasi genap dan hanya mencetak angka ganjil

# Program ini mendemonstrasikan penggunaan pernyataan break dan continue dalam loop di Python.