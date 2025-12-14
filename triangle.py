tinggi = int(input("Masukkan tinggi : "))
# Loop untuk setiap baris
for i in range(tinggi):
    # Mencetak spasi di sebelah kiri
    # Jumlah spasi berkurang seiring bertambahnya baris
    for j in range(tinggi - i - 1):
        print(" ", end="")

    # Mencetak bintang
    # Jumlah bintang bertambah seiring bertambahnya baris
    for k in range(2 * i + 1):
        print("*", end="")

    # Pindah ke baris baru
    print()

# Program ini mencetak segitiga bintang berdasarkan tinggi yang dimasukkan pengguna.