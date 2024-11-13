from functools import reduce

nilai_mahasiswa = {
    'Zaidun' : 99,
    'Suwarsono' : 100,
    'Dedi' : 75,
    'Joko' : 40,
    'Rusdi' : 78,
    'Diki' : 100,
    'Ansori' : 92,
    'Andri' : 76,
    'Kahfi' : 58,
    'Edi' : 77,
    'Joko' : 15,
    'Sutadi' : 90,
    'Made' : 55,
    'Nyoto' : 88,
    'Widodo' : 100
}

total_nilai = sum(nilai_mahasiswa.values())
nilai_tertinggi = max(nilai_mahasiswa.values())
mahasiswa_lulus = {nama: nilai for nama, nilai in nilai_mahasiswa.items() if nilai >= 75}
nilai_mahasiswa_update = {nama: nilai + 5 if nilai < 75 else nilai for nama, nilai in nilai_mahasiswa.items()}

# tampilkan nilai
print("Total nilai mahasiswa:", total_nilai)
print("Nilai tertinggi:", nilai_tertinggi)
print("Mahasiswa yang lulus:", mahasiswa_lulus)
print("Nilai mahasiswa setelah ditambahkan:", nilai_mahasiswa_update)

from functools import reduce

total_nilai = reduce(lambda x, y: x + y, nilai_mahasiswa.values())
print(total_nilai)
nilai_tertinggi = reduce(lambda x, y: x if x > y else y, nilai_mahasiswa.values())
print(nilai_tertinggi)
nilai_lulus = dict(filter(lambda x: x[1] >= 75, nilai_mahasiswa.items()))
print(nilai_lulus)
nilai_mahasiswa_update = dict(map(lambda x: (x[0], x[1] + 5) if x[1] < 75 else x, nilai_mahasiswa.items()))
print(nilai_mahasiswa_update)