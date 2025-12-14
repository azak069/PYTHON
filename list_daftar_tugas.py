tasks = []

def tampilkan_menu():
    print("=== Aplikasi To-Do List Tugas ===")
    print("1. Tambah Tugas")
    print("2. Lihat Semua Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")
    print("===========================\n")

def tambah_tugas():
    tugas_baru = input("Masukkan tugas yang ingin ditambahkan : ")
    tasks.append(tugas_baru)
    print(f"Tugas '{tugas_baru}' berhasil ditambahkan!")
    print("===========================\n")

def lihat_tugas():
    if not tasks:
        print("Daftar tugas masih kosong.")
        print("=========================\n")
    else:
        print("Daftar Tugas Anda :")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print("==========================\n")

def hapus_tugas():
    lihat_tugas()

    if not tasks:
        return

    try:
        nomor_tugas = int(input("Masukkan nomor tugas yang ingin dihapus : \n"))

        if 1 <= nomor_tugas <= len(tasks):
            tugas_dihapus = tasks.pop(nomor_tugas - 1)
            print(f"Tugas '{tugas_dihapus}' berhasil dihapus!")
        else:
            print("Nomor tidak valid! Silakan coba lagi.")

    except ValueError:
        print("Input tidak valid! Tolong masukkan angka.")

    print("===========================\n")

def main():
    while True:

        tampilkan_menu()
        pilihan = input("Pilih opsi (1-4)! : ")
        print("===========================\n")

        if pilihan == "1":
            tambah_tugas()
        elif pilihan == "2":
            lihat_tugas()
        elif pilihan == "3":
            hapus_tugas()
        elif pilihan == "4":
            print("Terimakasih telah menggunakan aplikasi ini. Sampai jumpa!\n")
            break
        else:
            print("Pilihan tidak valid! Silahkan pilih antara 1-4.")
            
        print("===========================\n")

if __name__ == "__main__":
    main()

# Program ini adalah aplikasi to-do list sederhana yang memungkinkan pengguna untuk menambah, melihat, dan menghapus tugas menggunakan fungsi di Python.