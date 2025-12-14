data = """
joko
170 cm
55 kg
"""

print(data)
# Menampilkan string multi-baris

nama = "joko"
tinggi = 170
data = "Nama saya " + nama + ", tinggi saya " + str(tinggi) + " cm"
print(data)
# Menggabungkan string dengan tipe data lain menggunakan konversi eksplisit

print(len(nama)) # Menghitung panjang string
print(len(data))

print(nama[0]) # Mengakses karakter dari string berdasarkan indeks
print(nama[1])  
print(data[0:9]) # Mengakses substring dari indeks 0 sampai 8
print(data[10:19])
print(data[11:]) # Mengakses substring dari indeks 11 sampai akhir
print(data[:9]) # Mengakses substring dari awal sampai indeks 8
print(nama[-1]) # Mengakses karakter dari belakang berdasarkan indeks
print(nama[-2])
print(data[-3:])

nama = " albert camus "
nama_upper = nama.upper() # Mengubah semua karakter menjadi huruf besar
print(nama_upper)
nama_lower = nama.lower() # Mengubah semua karakter menjadi huruf kecil
print(nama_lower)
nama_title = nama.title() # Mengubah karakter pertama setiap kata menjadi huruf besar
print(nama_title)
nama_capitalize = nama.capitalize() # Mengubah karakter pertama kalimat menjadi huruf besar
print(nama_capitalize)
nama_replace = nama.replace("camus", "einstein") # Mengganti kata "camus" dengan "einstein"
print(nama_replace)
nama_strip = nama.strip() # Menghapus spasi di awal dan akhir string
print(nama_strip)
nama_split = nama.split(" ") # Memisahkan string menjadi list berdasarkan spasi
print(nama_split)
jumlah_a = nama.count("a") # Menghitung jumlah kemunculan karakter "a"
print(jumlah_a)
posisi_r = nama.find("r") # Mencari posisi karakter "r" dalam string
print(posisi_r)
index_t = nama.index("t") # Mencari indeks karakter "t" dalam string
print(index_t)

kalimat = "Socrates hidup\nSocrates mati"
print(kalimat)
# Menggunakan newline untuk membuat baris baru dalam string

data = "Nama :\tJoko\nTinggi :\t170 cm\nBerat :\t55 kg"
print(data)
# Menggunakan tab dan newline untuk format string yang lebih rapi

path = "C:\\User\\Joko\\Documents"
print(path)
# Menampilkan backslash dalam string dengan dua backslash

sapa = "Dia berkata, \"Halo! Apa kabar?\" pada saya."
print(sapa)
# Menampilkan tanda kutip ganda dalam string dengan backslash

ekspresi = 'It\'s a beautiful day!'
print(ekspresi)
# Menampilkan tanda kutip tunggal dalam string dengan backslash

nama = "Plato"
umur = 80
kota = "Athena"
data = f"Nama saya {nama}, umur saya {umur} tahun, saya tinggal di {kota}."
print(data)
# Menggunakan f-string untuk menggabungkan string dengan variabel

panjang = 7
lebar = 5
luas = f"Luas persegi panjang dengan panjang {panjang} cm dan lebar {lebar} cm adalah {panjang * lebar} cm²."
print(luas)
# Menggunakan ekspresi dalam f-string untuk perhitungan langsung

nama = "leo tolstoy"
data = f"Nama saya {nama.title()}."
print(data)
# Menggunakan metode string dalam f-string untuk memformat teks

umur = 82
teks = "Nama saya {}. Umur saya {} tahun.".format(nama, umur)
print(teks)
# Menggunakan metode format() untuk menggabungkan string dengan variabel

# Program ini mendemonstrasikan berbagai operasi dan metode string di Python.