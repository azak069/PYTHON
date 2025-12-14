hobi = {"membaca", "menulis", "berkebun"} # membuat set
print(hobi) # menampilkan seluruh elemen dalam set

hobi.add("bersepeda") # menambahkan elemen baru
print(hobi)

hobi.remove("menulis") # menghapus elemen
print(hobi)

for e in hobi:
    print(f"Saya suka {e}") # mengiterasi setiap elemen dalam set

# Program ini mendemonstrasikan operasi dasar pada set di Python.