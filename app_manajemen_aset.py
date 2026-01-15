class Aset:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

class Kendaraan(Aset):
    def __init__(self, kode, nama, harga, jenis, tahun):
        super().__init__(kode, nama, harga)
        self.jenis = jenis 
        self.tahun = tahun

class Elektronik(Aset):
    def __init__(self, kode, nama, harga, kategori, garansi):
        super().__init__(kode, nama, harga)
        self.kategori = kategori
        self.garansi = garansi

class TanahBangunan(Aset):
    def __init__(self, kode, nama, harga, lokasi, luas):
        super().__init__(kode, nama, harga)
        self.lokasi = lokasi
        self.luas = luas

class DaftarAset:
    def __init__(self):
        self.daftar_aset = []

    def tambah_aset(self, aset):
        self.daftar_aset.append(aset)

    def ambil_aset(self, kode):
        for aset in self.daftar_aset:
            if aset.kode == kode:
                return aset
        return None
    
    def hapus_aset(self, kode):
        aset = self.ambil_aset(kode)
        for i, a in enumerate(self.daftar_aset):
            if a.kode == kode:
                del self.daftar_aset[i]
                return True
        return False
        

class App:
    def __init__(self):
        self.daftar_aset = DaftarAset()

    def jalankan(self):
        while True:
            print("\n=== Aplikasi Manajemen Aset Sederhana Berbasis OOP ===")
            print("Selamat datang di aplikasi manajemen aset sederhana berbasis OOP!")
            print("1. Tambah Aset")
            print("2. Tampilkan Daftar Aset")
            print("3. Keluar")
            pilih = int(input("Pilih menu (1-3): "))

            if pilih == 1:
                self.tambah_aset()
            elif pilih == 2:
                self.tampilkan_daftar_aset()
            elif pilih == 3:
                print("Terima kasih telah menggunakan aplikasi manajemen aset sederhana.")
                break

    def tambah_aset(self):
        while True:
            print("\nPilih Jenis Aset yang Ingin Ditambahkan:")
            print("1. Kendaraan")
            print("2. Elektronik")
            print("3. Tanah dan Bangunan")
            print("4. Kembali ke Menu Utama")
            pilih = int(input("Pilih jenis aset (1-4): "))

            if pilih == 1:
              self.tambah_kendaraan()
            elif pilih == 2:
                self.tambah_elektronik()
            elif pilih == 3:
                self.tambah_tanah_bangunan()
            elif pilih == 4:
                break
    
    def tambah_kendaraan(self):
        print("\nMenambahkan Aset Kendaraan:")
        kode = input("Masukkan kode aset: ")
        nama = input("Masukkan nama aset: ")
        harga = float(input("Masukkan harga aset: "))
        jenis = input("Masukkan jenis kendaraan (misal: Mobil, Motor): ")
        tahun = int(input("Masukkan tahun pembuatan kendaraan: "))

        kendaraan_baru = Kendaraan(kode, nama, harga, jenis, tahun)
        self.daftar_aset.tambah_aset(kendaraan_baru)
        print("Aset kendaraan berhasil ditambahkan.")

    def tambah_elektronik(self):
        print("\nMenambahkan Aset Elektronik:")
        kode = input("Masukkan kode aset: ")
        nama = input("Masukkan nama aset: ")
        harga = float(input("Masukkan harga aset: "))
        kategori = input("Masukkan kategori elektronik (misal: Laptop, Smartphone): ")
        garansi = int(input("Masukkan masa garansi (dalam bulan): "))

        elektronik_baru = Elektronik(kode, nama, harga, kategori, garansi)
        self.daftar_aset.tambah_aset(elektronik_baru)
        print("Aset elektronik berhasil ditambahkan.")
    
    def tambah_tanah_bangunan(self):
        print("\nMenambahkan Aset Tanah dan Bangunan:")
        kode = input("Masukkan kode aset: ")
        nama = input("Masukkan nama aset: ")
        harga = float(input("Masukkan harga aset: "))
        lokasi = input("Masukkan lokasi tanah/bangunan: ")
        luas = float(input("Masukkan luas tanah/bangunan (dalam m2): "))

        tanah_bangunan_baru = TanahBangunan(kode, nama, harga, lokasi, luas)
        self.daftar_aset.tambah_aset(tanah_bangunan_baru)
        print("Aset tanah dan bangunan berhasil ditambahkan.")

    def tampilkan_daftar_aset(self):
        if not self.daftar_aset.daftar_aset:
            print("\nDaftar aset kosong.")
            return

        print("\n=== Daftar Aset ===")
        for aset in self.daftar_aset.daftar_aset:
            if isinstance(aset, Kendaraan):
                print("\nAset Kendaraan")
                print(f"Kode: {aset.kode}")
                print(f"Nama: {aset.nama}")
                print(f"Harga: {aset.harga}")
                print(f"Jenis: {aset.jenis}")
                print(f"Tahun: {aset.tahun}")
            elif isinstance(aset, Elektronik):
                print("\nAset Elektronik")
                print(f"Kode: {aset.kode}")
                print(f"Nama: {aset.nama}")
                print(f"Harga: {aset.harga}")
                print(f"Kategori: {aset.kategori}")
                print(f"Garansi: {aset.garansi} bulan")
            elif isinstance(aset, TanahBangunan):
                print("\nAset Tanah dan Bangunan")
                print(f"Kode: {aset.kode}")
                print(f"Nama: {aset.nama}")
                print(f"Harga: {aset.harga}")
                print(f"Lokasi: {aset.lokasi}")
                print(f"Luas: {aset.luas} m2")

        print ("\n== Kelola Aset ==")
        print("1. Ubah Aset")
        print("2. Hapus Aset")
        print("3. Kembali ke Menu Utama")
        pilih = int(input("Pilih opsi (1-3): "))

        if pilih == 1:
            self.ubah_aset()
        elif pilih == 2:
            self.hapus_aset()

    def hapus_aset(self):
        kode = input("\nMasukkan kode aset yang ingin dihapus: ")
        berhasil = self.daftar_aset.hapus_aset(kode)
        if berhasil:
            print(f"Aset dengan kode {kode} berhasil dihapus!")
        else:
            print(f"Aset dengan kode {kode} tidak ditemukan!")

    def ubah_aset(self):
        kode = input("\nMasukkan kode aset yang ingin diubah: ")
        aset = self.daftar_aset.ambil_aset(kode)
        if aset is None:
            print(f"Aset dengan kode {kode} tidak ditemukan!")
            return

        else:
            if isinstance(aset, Kendaraan):
                nama = input("Masukkan nama aset baru: ")
                harga = float(input("Masukkan harga aset baru: "))
                jenis = input("Masukkan jenis kendaraan baru: ")
                tahun = int(input("Masukkan tahun pembuatan kendaraan baru: "))
                aset.nama = nama
                aset.harga = harga
                aset.jenis = jenis
                aset.tahun = tahun
            elif isinstance(aset, Elektronik):
                nama = input("Masukkan nama aset baru: ")
                harga = float(input("Masukkan harga aset baru: "))
                kategori = input("Masukkan kategori elektronik baru: ")
                garansi = int(input("Masukkan masa garansi baru (dalam bulan): "))
                aset.nama = nama
                aset.harga = harga
                aset.kategori = kategori
                aset.garansi = garansi
            elif isinstance(aset, TanahBangunan):
                nama = input("Masukkan nama aset baru: ")
                harga = float(input("Masukkan harga aset baru: "))
                lokasi = input("Masukkan lokasi tanah/bangunan baru: ")
                luas = float(input("Masukkan luas tanah/bangunan baru (dalam m2): "))
                aset.nama = nama
                aset.harga = harga
                aset.lokasi = lokasi
                aset.luas = luas

            print("Aset berhasil diubah!")

if __name__ == "__main__":
    app = App()
    app.jalankan()

# Program ini menjalankan aplikasi manajemen atau pengelolaan aset sederhana yang berbasis OOP dalam Python.