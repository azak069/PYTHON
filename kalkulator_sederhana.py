def penjumlahan():
    print("=== Program Penjumlahan ===")
    try:
        angka1 = int(input("Angka 1: "))
        angka2 = int(input("Angka 2: "))
        hasil = angka1 + angka2
        print(f"Hasil penjumlahan : {hasil}")
        print("=== Program Penjumlahan Selesai ===")
    except TypeError:
        print("Input tidak valid! Tolong masukkan angka")
    except ValueError:
        print("Input tidak valid! Tolong masukkan angka")
    print("====================================\n")

def pengurangan():
    print("=== Program Pengurangan ===")
    try:
        angka1 = int(input("Angka 1: "))
        angka2 = int(input("Angka 2: "))
        hasil = angka1 - angka2
        print(f"Hasil pengurangan : {hasil}")
        print("=== Program Pengurangan Selesai ===")
    except TypeError:
        print("Input tidak valid! Tolong masukkan angka")
    except ValueError:
        print("Input tidak valid! Tolong masukkan angka")
    print("====================================\n")

def perkalian():
    print("=== Program Perkalian ===")
    try:
        angka1 = int(input("Angka 1: "))
        angka2 = int(input("Angka 2: "))
        hasil = angka1 * angka2
        print(f"Hasil perkalain : {hasil}")
        print("=== Program Perkalian Selesai ===")
    except TypeError:
        print("Input tidak valid! Tolong masukkan angka")
    except ValueError:
        print("Input tidak valid! Tolong masukkan angka")
    print("====================================\n")

def pembagian():
    print("=== Program Pembagian ===")
    try:
        angka1 = int(input("Angka 1: "))
        angka2 = int(input("Angka 2: "))
        hasil = angka1 / angka2
        print(f"Hasil pembagian : {hasil}")
        print("=== Program Pembagian Selesai ===")
    except ZeroDivisionError:
        print("Tidak bisa dibagi nol! Silakan coba lagi.")
    except ValueError:
        print("Input tidak valid! Tolong masukkan angka.")
    except TypeError:
        print("Input tidak valid! Tolong masukkan angka")
    print("====================================\n")

def menu():
    while True:
        print("=== Program Kalkulator Sederhana ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        print("====================================\n")

        try:
            pilihan = int(input("Pilihan Anda : "))

            if pilihan == 1:
                penjumlahan()
            elif pilihan == 2:
                pengurangan()
            elif pilihan == 3:
                perkalian()
            elif pilihan == 4:
                pembagian()
            elif pilihan == 5:
                print("Terimakasih telah menggunakan program ini!")
                print("=== Program Kalkulator Sederhana Selesai ===\n")
                break
            else:
                print("Pilihan tidak valid! Tolong pilih 1-5.\n")
                
        except ValueError:
            print("Pilihan tidak valid! Tolong masukkan angka.\n")


menu()

# Program ini adalah kalkulator sederhana yang dapat melakukan penjumlahan, pengurangan, perkalian, dan pembagian menggunakan fungsi di Python.