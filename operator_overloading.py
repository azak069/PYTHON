# operator overloading dengan magic methods
class Apel:
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def __add__(self, other):
        return Apel(self.jumlah + other.jumlah)
    
    def __sub__(self, other):
        return Apel(self.jumlah - other.jumlah)
    
    def __mul__(self, other):
        return Apel(self.jumlah * other.jumlah)
    
    def __ed__(self, other):
        return Apel(self.jumlah == other.jumlah)
    
    def __lt__(self, other):
        return Apel(self.jumlah < other.jumlah)
    
    def __le__(self, other):
        return Apel(self.jumlah <= other.jumlah)
    
    def __gt__(self, other):
        return Apel(self.jumlah > other.jumlah)
    
    def __ge__(self, other):
        return Apel(self.jumlah >= other.jumlah)
    
    def __ne__(self, other):
        return Apel(self.jumlah != other.jumlah)
    
    def __str__(self):
        return f"Apel {self.jumlah}"
# mengoperasikan operator overloading dengan magic methods di dalam kelas
# agar objek yang dibuat bisa dioperasikan dalam aritmetika dan perbandingan 

apel1 = Apel(6)
apel2 = Apel(9)
apel3 = apel1 + apel2
apel4 = apel1 - apel2
apel5 = apel1 * apel2
apel6 = apel1 == apel2
apel7 = apel1 < apel2
apel8 = apel1 <= apel2
apel9 = apel1 > apel2
apel10 = apel1 >= apel2
apel11 = apel1 != apel2
print(apel3)
print(apel4)
print(apel5)
print(apel6)
print(apel7)
print(apel8)
print(apel9)
print(apel10)
print(apel11)

# Program ini mendemonstrasikan penggunaan operator overloading dengan magic methods dalam Object Oriented Programming Python.