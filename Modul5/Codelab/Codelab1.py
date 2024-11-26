import matplotlib.pyplot as plt

# Data mata kuliah
data_matkul = [
    ("Fungsional", 87.5, 48),
    ("Jarkom", 91, 52),
    ("Mobile", 79.7, 40),
    ("Pirdas", 92.5, 49),
    ("Web", 89, 55)
]

# Step 1: Ekstrak data dengan list comprehension
mata_kuliah = [data[0] for data in data_matkul]
avg_nilai = [data[1] for data in data_matkul]
jumlah_mahasiswa = [data[2] for data in data_matkul]

# Step 2: Hitung total nilai untuk setiap mata kuliah
total_nilai = list(map(lambda x: x[1] * x[2], data_matkul))

# Step 3: Scatter plot (hubungan rata-rata nilai dan jumlah mahasiswa)
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.title("Scatter Plot: Rata-rata Nilai vs Jumlah Mahasiswa")
plt.scatter(avg_nilai, jumlah_mahasiswa, color='blue', label="Data")
plt.xlabel("Rata-rata Nilai")
plt.ylabel("Jumlah Mahasiswa")
plt.grid(True)


# Step 4: Diagram batang (total nilai setiap mata kuliah)
plt.subplot(2, 2, 2)
plt.title("Bar Chart: Total Nilai")
plt.bar(mata_kuliah, total_nilai, color='orange')
plt.xlabel("Mata Kuliah")
plt.ylabel("Total Nilai")

# Step 5: Diagram garis (rata-rata nilai tiap mata kuliah)
plt.subplot(2, 2, 3)
plt.title("Line Chart: Rata-rata Nilai")
plt.plot(mata_kuliah, avg_nilai, marker='o', linestyle='-', color='green')
plt.ylim(0, 100)
plt.xlabel("Mata Kuliah")
plt.ylabel("Rata-rata Nilai")

# Step 6: Pie chart
plt.subplot(2, 2, 4)
# explode
explode = [0, 0, 0.1, 0, 0]
plt.title("Pie Chart: Jumlah Mahasiswa")
plt.pie(jumlah_mahasiswa, labels=mata_kuliah, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)

# Step 7: Tampilkan subplot
plt.tight_layout()
plt.show()
