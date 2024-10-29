from functools import reduce

# def aritmetika(a, d, n):
#     return [a + i * d for i in range(n)]


# def geometri(a, r, n):
#     return [a * (r ** i) for i in range(n)]


def jumlahkan(x, y):
    return x + y
    
def aritmetika_geometri(a, d, r, n):
    if n == 1:
        return [a]
    else:
        new_var = aritmetika_geometri(a, d, r, n - 1)
        suku_ke_n = (a + (n - 1) * d) * (r ** (n - 1))
        return new_var + [suku_ke_n]

# Parameter
a = 4    # suku pertama
d = 3    # aritmetika
r = 2    # geometri
n = 6    # jumlah suku

# baris_aritmetika = aritmetika(a, d, n)
# baris_geometri = geometri(a, r, n)
baris_aritmetika_geometri = aritmetika_geometri(a, d, r, n)

# print("Baris Aritmetika:", baris_aritmetika)
# print("Baris Geometri:", baris_geometri)
print("Baris Aritmetika-Geometri:", baris_aritmetika_geometri)

# jumlah_aritmetika = reduce(jumlahkan, baris_aritmetika)
# jumlah_geometri = reduce(jumlahkan, baris_geometri)
jumlah_aritmetika_geometri = reduce(jumlahkan, baris_aritmetika_geometri)

# print("\nJumlah Deret Aritmetika:", jumlah_aritmetika)
# print("Jumlah Deret Geometri:", jumlah_geometri)
print("Jumlah Deret Aritmetika-Geometri:", jumlah_aritmetika_geometri)
