# set adalah kumpulan unik yang tidak berurutan
hobi = {"membaca", "menulis", "berkebun"} # membuat set
print(hobi) # menampilkan seluruh elemen dalam set
# set tidak mendukung pengindeksan, jadi kita tidak bisa mengakses elemen dengan indeks seperti pada list

hobi.add("bersepeda") # menambahkan elemen baru
print(hobi)

hobi.remove("menulis") # menghapus elemen
print(hobi)

for e in hobi:
    print(f"Saya suka {e}") # mengiterasi setiap elemen dalam set

angka1 = {1, 2, 3, 4, 5}
angka2 = {3, 4, 5, 6, 7}

union_set = angka1.union(angka2) # menggabungkan dua set
print("Union:", union_set)

difference_set = angka1.difference(angka2) # elemen yang ada di angka1 tapi tidak di angka2
print("Difference:", difference_set)

symetric_difference_set = angka1.symmetric_difference(angka2) # elemen yang ada di salah satu set tapi tidak di keduanya
print("Symmetric Difference:", symetric_difference_set)

intersection_set = angka1.intersection(angka2) # elemen yang ada di kedua set
print("Intersection:", intersection_set)

# Program ini mendemonstrasikan operasi dasar pada set di Python.