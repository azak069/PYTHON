hari = int(input("Masukkan nama hari : ")).lower()
# menggunakan match case untuk mengecek variabel hari
match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("KERJA KERJA KARJA")
    case "sabtu" | "minggu":
        print("LIBUR BRO")
    case _:
        print("Nama hari tidak valid!")

# Program ini mendemonstrasikan penggunaan match case di Python untuk mengecek nama hari.