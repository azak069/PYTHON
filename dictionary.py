profile = {
    "nama": "zaki",
    "umur": 20,
    "asal": "Magelang"
} # membuat dictionary dengan beberapa pasangan kunci-nilai

profile["pekerjaan"] = "programmer"  # menambahkan pasangan kunci-nilai baru
profile["umur"] = 18  # mengubah nilai berdasarkan kunci
print(profile["nama"])  # mengakses nilai berdasarkan kunci
print(profile.get("asal"))  # mengakses nilai menggunakan metode get()
profile.pop("pekerjaan")  # menghapus pasangan kunci-nilai berdasarkan kunci
print(profile)

data = {1 : "zaki",2 : 22,3 : "Magelang"}
# mengakses dan menampilkan nilai dari dictionary dengan format tertentu
print(f"Nama saya : {data[1]}. Umur : {data[2]}. Asal : {data[3]}.")

# Program ini mendemonstrasikan penggunaan dictionary di Python.