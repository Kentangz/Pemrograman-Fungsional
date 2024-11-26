import matplotlib.pyplot as plt
import numpy as np

data_matkul = [
    ("Fungsional", 87.5, 48),
    ("Jarkom", 91, 52),
    ("Mobile", 79.7, 40),
    ("Pirdas", 92.5, 49),
    ("Web", 89, 55)
]

mata_kuliah = [data[0] for data in data_matkul]
avg_nilai = [data[1] for data in data_matkul]
jumlah_mahasiswa = [data[2] for data in data_matkul]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Rata-rata Nilai")
plt.scatter(mata_kuliah, avg_nilai)
plt.plot(mata_kuliah, avg_nilai, linestyle='--')
plt.ylim(0, 100)

plt.subplot(2, 2, 4)
plt.title("Jumlah mahasiswa")
plt.scatter(mata_kuliah, jumlah_mahasiswa)
plt.plot(mata_kuliah, jumlah_mahasiswa, color='green')

plt.subplot(3, 2, 2)
explode = [0, 0, 0.15, 0, 0]
plt.title("Jumlah Mahasiswa")
plt.pie(jumlah_mahasiswa, labels=mata_kuliah, explode=explode, shadow = True)
plt.show()
