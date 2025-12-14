password_true = "etcode99"
percobaan = 0
max_percobaan = 3
# menggunakan loop while yang akan terus berjalan selama percobaan kurang dari maksimal percobaan
while percobaan < max_percobaan:
    password_input = input("Masukkan password: ")

    if password_input == password_true:
        print("Akses diterima.")
        break
    else:
        percobaan += 1
        print(f"Password salah. Percobaan ke-{percobaan} dari {max_percobaan}.")
# jika percobaan telah mencapai maksimal, tampilkan pesan akses ditolak di luar loop
else:
    print("Akses ditolak. Terlalu banyak percobaan gagal.")

# Program ini mendemonstrasikan penggunaan loop while untuk membatasi jumlah percobaan memasukkan password di Python.