# import function_m as f # mengimpor module file function_m.py dengan alias f

# sapa = f.sapa("Zaki") # memanggil fungsi sapa dari module file function_m.py
# total = f.total(10,20,30,40,50)
# print(sapa)
# print(total)

from function_m import sapa # mengimpor fungsi sapa dari module file function_m.py
from function_m import total

sapa("Bill") # memanggil fungsi sapa dari module file function_m.py
print(total(15, 25, 35, 45, 55))

# Program ini menggunakan import module untuk mengakses fungsi dalam file function_m.py