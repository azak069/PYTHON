import random

class Soal:
    def __init__(self, pertanyaan, jawaban, jawaban_benar):
        self.pertanyaan = pertanyaan
        self.jawaban = jawaban
        self.jawaban_benar = jawaban_benar
        random.shuffle(self.jawaban)

    def cek_jawaban(self, jawaban_user):
        return jawaban_user == self.jawaban_benar


class Ujian:
    def __init__(self, soal_real):
        self.soal_ujian = []
        random.shuffle(soal_real)
        for i in range(10):
            try:
                soal = soal_real[i]
                data = soal.split("|", 1)
                if len(data) < 2:
                    raise ValueError("Setiap soal harus memiliki minimal 2 pilihan jawaban.")
                pertanyaan = data[0].strip()
                semua_jawaban = data[1].strip()
                jawaban = [j.strip() for j in semua_jawaban.split(",") if j.strip()]
                jawaban_benar = jawaban[0]

                soal = Soal(pertanyaan, jawaban, jawaban_benar)
                self.soal_ujian.append(soal)
            except Exception as e:
                print(f"Gagal memproses soal: {soal}. Error: {e}")
                continue

        if not self.soal_ujian:
            raise ValueError("Tidak ada soal yang valid untuk ujian setelah pemrosesan.")
    
class App:
    def __init__(self, file):
        soal_real = []
        try:
            with open(file, "r") as file:
                for line in file:
                    soal_real.append(line.strip())
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file}' tidak ditemukan. Pastikan file tersebut ada di direktori yang benar.")
        
        self.ujian = Ujian(soal_real)

    def jalankan_ujian(self):
        opsi = ["A", "B", "C", "D"]
        jawaban_benar = 0
        jawaban_salah = 0

        for j, soal in enumerate(self.ujian.soal_ujian):
            soal = self.ujian.soal_ujian[j]
            print("\n", j + 1, ".", soal.pertanyaan)
            print("Jawaban : ")

            for k, jawaban in enumerate(soal.jawaban):
                label = opsi[k] if k < len(opsi) else f"({k+1})"
                print(label, ".", jawaban)

            while True:
                jawaban_user = input("Jawaban (A/B/C/D): ").strip().upper()
                if not jawaban_user:
                    print("Input kosong. Tolong masukkan jawaban!")
                    continue
                if jawaban_user not in opsi[:len(soal.jawaban)]:
                    print("Jawaban tidak valid. Silakan masukkan salah satu dari :", ", ".join(opsi[:len(soal.jawaban)]))
                    continue
                break
            try:
                jawaban_index = opsi.index(jawaban_user)
                jawaban_asli = soal.jawaban[jawaban_index]

                if soal.cek_jawaban(jawaban_asli):
                    print("Jawaban Anda BENAR!")
                    jawaban_benar += 1
                else:
                    print("Jawaban Anda SALAH!")
                    jawaban_salah += 1
            except ValueError:
                print("Terjadi kesalahan dalam jawaban Anda. Soal ini dilewati.")
                jawaban_salah += 1
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
                jawaban_salah += 1                

        total = jawaban_benar + jawaban_salah
        if total == 0:
            print("\nTidak ada soal yang dijawab.")
            return
        nilai = (jawaban_benar / total) * 100
        print("Hasil Ujian :")
        print("Jawaban Benar : ", jawaban_benar)
        print("Jawaban Salah : ", jawaban_salah)
        print("Nilai Ujian : {:.2f}%".format(nilai))

if __name__ == "__main__":
    try:
        app = App("bank_soal.txt")
        app.jalankan_ujian()
    except Exception as e:
        print(f"Gagal menjalankan aplikasi ujian: {e}")
    print("Terima kasih telah menggunakan aplikasi ujian sekolah berbasis OOP.")

# Program ini merekonstruksi kembali program ujian sekolah menggunakan pendekatan berorientasi objek (OOP) dalam Python.
# Fungsi-fungsi utama telah diubah menjadi kelas dan methods untuk meningkatkan modularitas dan pemeliharaan kode.
# Buatlah file teks bernama "bank_soal.txt" dengan format soal yang sesuai agar program dapat berjalan dengan baik.
# Format soal dalam file teks adalah sebagai berikut:Pertanyaan|Jawaban1(Jawaban Benar),Jawaban2,Jawaban3,Jawaban4,...