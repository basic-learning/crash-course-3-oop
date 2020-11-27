from geometri.bangun_datar import BangunDatar
from geometri.persegi_panjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('Menggunakan OOP')

p1 = PersegiPanjang(10,3)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(4, 8)
print(s1.info())
print(s1.hitung_luas())

print('\nMencoba membuat object dari kelas BangunDatar')
b1 = BangunDatar()
print(b1.info)
print(b1.hitung_luas)

# Polymorphism : Kemampuan object untuk merespons berbeda terhadap pemanggilan method yang sama
daftar_bangun_datar = []
daftar_bangun_datar.append(p1)
daftar_bangun_datar.append(s1)
print('\nPolymorphism')
for bangun_datar in daftar_bangun_datar:
    print(bangun_datar.info())