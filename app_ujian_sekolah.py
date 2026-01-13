import random
import os

def ambil_soal(nama_file="bank_soal.txt"):
    soal_real = []
    try:
        with open("bank_soal.txt", encoding="utf-8") as file:
            for line in file:
                soal_real.append(line.strip())
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{nama_file}' tidak ditemukan. Pastikan file tersebut ada di direktori yang benar.")
    return soal_real

def buat_soal(jumlah=10, nama_file="bank_soal.txt"):
    soal_real = ambil_soal(nama_file)

    if not soal_real:
        raise ValueError("Tidak ada soal yang tersedia dalam bank soal.")

    jumlah_soal = min(jumlah, len(soal_real))
   
    random.shuffle(soal_real)
    sampel_soal = soal_real[:jumlah_soal]

    soal_ujian = []
    for soal in sampel_soal:
        try:
            data = soal.split("|", 1)
            if len(data) < 2:
                raise ValueError("Setiap soal harus memiliki minimal 2 pilihan jawaban.")
            pertanyaan = data[0].strip()
            semua_jawaban = data[1].strip()
            jawaban = [j.strip() for j in semua_jawaban.split(",") if j.strip()]

            jawaban_benar = jawaban[0]

            random.shuffle(jawaban)

            soal_ujian.append({
                "pertanyaan": pertanyaan,
                "jawaban": jawaban,
                "jawaban_benar": jawaban_benar,
            })
        except Exception as e:
            print(f"Gagal memproses soal: {soal}. Error: {e}")
            continue

    if not soal_ujian:
        raise ValueError("Tidak ada soal yang valid untuk ujian setelah pemrosesan.")
    
    return soal_ujian

def app_ujian():
    try:
        soal_ujian = buat_soal()
    except Exception as e:
        print(f"Gagal membuat soal ujian: {e}")
        return
    
    jawaban_benar = 0
    jawaban_salah = 0

    for j, soal in enumerate(soal_ujian):
        opsi = ["A", "B", "C", "D"]
        print("\nPertanyaan", j + 1, ".", soal["pertanyaan"])
        print("Jawaban : ")

        for k, jawaban in enumerate(soal["jawaban"]):
            label = opsi[k] if k < len(opsi) else f"({k+1})"
            print(label, ".", jawaban)

        while True:
            jawaban_user = input("Jawaban (A/B/C/D): ").strip().upper()
            if not jawaban_user:
                print("Input kosong. Tolong masukkan jawaban!")
                continue
            if jawaban_user not in opsi[:len(soal["jawaban"])]:
                print("Jawaban tidak valid. Silakan masukkan salah satu dari :", ", ".join(opsi[:len(soal["jawaban"])]))
                continue
            break
        try:
            jawaban_index = opsi.index(jawaban_user)
            jawaban_asli = soal["jawaban"][jawaban_index]

            if jawaban_asli == soal["jawaban_benar"]:
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

app_ujian()

# Program ini adalah aplikasi ujian sekolah sederhana yang mengambil soal dari file teks, mengacak soal dan jawaban, serta menghitung hasil ujian berdasarkan jawaban pengguna.
# Buatlah file teks bernama "bank_soal.txt" dengan format soal yang sesuai agar program dapat berjalan dengan baik.
# Format soal dalam file teks adalah sebagai berikut:Pertanyaan|Jawaban1(Jawaban Benar),Jawaaban2,Jawaaban3,Jawaban4,...