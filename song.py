import sys as s
import time as t

lirik = [
    ("Dunia pasti ada akhirnya", 0.17),
    ("Bintang-bintang pun ada umurnya", 0.16),
    ("Maka tenang saja, kita di sini berdua", 0.15),
    ("Aaaa", 0.25),
    ("Nikmati sementara yang ada", 0.15)
]

jeda = [1.0, 1.0, 0.5, 2.25, 3.0]
for i, (baris, jeda_k) in enumerate(lirik):
    for kata in baris:
        print(kata, end="")
        s.stdout.flush()
        t.sleep(jeda_k)
    t.sleep(jeda[i])
    print(" ")

# Program ini menampilkan lirik lagu dengan efek ketikan menggunakan modul sys dan time di Python.
        
            
        
