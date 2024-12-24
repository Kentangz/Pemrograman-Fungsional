def hitung_luas_persegi(sisi):
    return sisi * sisi


luas_persegi = hitung_luas_persegi(5)
print(luas_persegi)

angka = [2, 4, 6, 8]
first_element = angka[0]
sum_of_elements = sum(angka)    
sorting_elements = sorted(angka, reverse=True)

print("angka pertama", first_element)
print("jumlah angka",sum_of_elements)
print("urutan menurun", sorting_elements)

teks = "Pemrograman Fungsional"
uppercase = teks.upper()
sum_of_vocals = sum([1 for char in teks if char in "aiueoAIUEO"])

print("uppercase", uppercase)
print("jumlah karakter", sum_of_vocals)

def kelipatan_tiga(n):
    return [i for i in n if i % 3 == 0]

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

hasil = kelipatan_tiga(n)
print(hasil)

def bilangan_genap(batas):
    n = 0
    while n <= batas:
        yield n
        n += 2

generator_genap = bilangan_genap(10)

# Cetak menggunakan for loop
for num in generator_genap:
    print(num, end=" ")


generator_genap = bilangan_genap(10)
print("\n next():")
print(next(generator_genap))  # 0
print(next(generator_genap))  # 2
print(next(generator_genap))  # 4

def fibonanci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonanci_gen()

for i in range(10):
    print(next(gen), end=" ")

angka = [1, 2, 3, 4, 5]
mapping = map(lambda x: x * 2, angka)
print(list(mapping))

angka = [10, 15, 20, 25, 30]
filtering = filter(lambda x: x % 2 == 0, angka)
print(list(filtering))

from functools import reduce
angka = [1, 2, 3, 4, 5]
reducing = reduce(lambda x, y: x * y, angka)
print(reducing)

ganjil = [i for i in range(20) if i % 2 != 0]
print(ganjil)

def pengurang(a):
    def kurangi(b):
        return b-a
    return kurangi

kurang_dua = pengurang(2)(5)
print(kurang_dua)

lambda_perkalian = lambda a,b: a*b
print(lambda_perkalian(2,3))



def pembuat_kali(n):
    return lambda x: x * n

kali_tiga = pembuat_kali(3)
print(kali_tiga(5))


def imp_decorator(func):
    def wrapper(*args, **kwargs):
        print("Sebelum eksekusi")
        func(*args, **kwargs)
        print("Setelah eksekusi")
    return wrapper

@imp_decorator
def contoh():
    print("contoh decorator")

contoh()


import matplotlib.pyplot as plt
data_x = [0, 1, 2, 3, 4]
data_y = [0, 1, 4, 9, 16]

plt.plot(data_x, data_y)
plt.show()

Informatika = 50
Sistem_Informasi = 30
Teknik_Komputer = 20

plt.bar (['Informatika', 'Sistem_Informasi', 'Teknik_Komputer'], [Informatika, Sistem_Informasi, Teknik_Komputer])
plt.show()

x = [1, 2, 3, 4, 5]
y = [5, 7, 6, 8, 7]

plt.scatter(x, y)
plt.show()

bulan = ["Jan", "Feb", "Mar", "Apr", "May"]
suhu = [25, 26, 27, 26, 25]

plt.plot(bulan, suhu)
plt.xlabel("Bulan")
plt.ylabel("Suhu")
plt.show()
