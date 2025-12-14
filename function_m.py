def sapa(nama):
    hello = print(f"Hallo, {nama}. Senang bertemu denganmu")
    return hello

def total(*angka):
    hasil = 0
    for i in angka:
        hasil += i
        return hasil
    
# Program ini membuat module berisi 2 fungsi yang bisa diimport ke program di file module.py