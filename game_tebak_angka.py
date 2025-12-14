def menu():
    while True:
        print("=== Program Tebak Angka ===")
        print("1. Tebak Angka")
        print("2. Keluar")
        print("===========================\n")

        try:
            pilihan = int(input("Pilihan Anda : "))

            if pilihan == 1:
                tebak_angka()
            elif pilihan == 2:
                print("Terimakasih telah menggunakan program ini!")
                print("=== Program Tebak Angka Selesai ===\n")
                break
            else:
                print("Pilihan tidak valid! Silakan masukkan 1 atau 2.\n")
        except ValueError:
            print("Pilihan tidak valid! Silakan masukkan angka.\n")

def tebak_angka():
    import random
    angka_acak = random.randint(1, 10)
    max_tebak = 3
    tebak = 0

    while tebak < max_tebak:
        tebak += 1
        try:
            angka_tebak = int(input("Masukkan Angka Tebakan Anda : "))
            if angka_tebak > angka_acak:
                print("Angka terlalu Besar!\n")
            elif angka_tebak < angka_acak:
                print("Angka terlalu Kecil!\n")
            else:
                print("Selamat! Tebakan Anda Benar!\n")
                break
        except ValueError:
            print("Input tidak valid! Silakan masukkan angka.\n")
        except TypeError:
            print("Input tidak valid! Silakan masukkan angka.\n")
    else:
        print("Sayang Sekali! Kamu telah melewati maksimal tebakan.")
        print("Angka yang benar adalah ", angka_acak)
        print("Terimakasih telah menebak!\n")

    input("Tekan Enter untuk kembali ke menu utama!\n")

menu()

# Program ini adalah permainan tebak angka sederhana menggunakan fungsi di Python.