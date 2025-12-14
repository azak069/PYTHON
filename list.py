nama = ["Jokowi", "Prabowo", "Ganjar", "Anies", "Sandiaga"] # membuat list
print(nama[0])  # Output: Jokowi
print(nama[2])  # Output: Ganjar
print(nama[1])  # Output: Prabowo
print(nama[0])  # Output: Jokowi
length = len(nama) # mendapatkan panjang list
print(length)  # Output: 5
print(nama.index("Ganjar"))  # mencari indeks elemen "Ganjar"

# Program Akses Elemen List Sederhana

nama = ["Jokowi", "Prabowo", "Ganjar", "Anies", "Sandiaga"]
print(nama)
nama[3] = "Ridwan Kamil" # mengubah elemen di indeks ke-3
print(nama)

# Program Mengubah Elemen List Sederhana

nama = ["Jokowi", "Prabowo", "Ganjar", "Anies", "Sandiaga"]
print(nama)
nama.append("Ahmad Dhani") # menambahkan elemen di akhir list
print(nama)
nama.insert(2, "Sri Mulyani") # menambahkan elemen di indeks tertentu
print(nama)
nama2 = nama.copy() # menyalin list
nama2.append("Ma'ruf Amin") # menambahkan elemen di list salinan
print(nama2)

# Program Menambahkan Elemen List Sederhana

nama.remove("Sandiaga") # menghapus berdasarkan nilai
print(nama)
nama.pop() # menghapus elemen terakhir
print(nama)
del nama[1] # menghapus berdasarkan indeks dengan del
print(nama)
nama.clear() # menghapus semua elemen dalam list
print(nama)

# Program Menghapus Elemen List Sederhana

nama = ["Jokowi", "Prabowo", "Ganjar", "Anies", "Sandiaga"]
umur = [61, 60, 54, 50, 49]
data_gabungan = nama + umur # menggabungkan dua list
print(data_gabungan)

# Program Menggabungkan Dua List Sederhana

nama = ["Jokowi", "Prabowo", "Ganjar", "Anies", "Sandiaga"]
for n in nama:
    print(f"Nama calon presiden: {n}") # iterasi elemen list
for i in range(0, len(nama)):
    print(f"Calon presiden ke-{i} adalah {nama[i]}") # iterasi dengan indeks

# Program Iterasi Elemen List Sederhana

if "Jokowi" in nama: # pengecekan keberadaan elemen
    print("Jokowi ada dalam daftar calon presiden.")
else:
    print("Jokowi tidak ada dalam daftar calon presiden.")

# Program Pengecekan Keberadaan Elemen List Sederhana

angka = [5, 2, 9, 1, 5, 6]
angka.sort() # mengurutkan list secara ascending
print(angka)
angka.reverse() # membalik urutan list
print(angka)

# Program ini mendemonstrasikan berbagai operasi dasar pada list di Python.
