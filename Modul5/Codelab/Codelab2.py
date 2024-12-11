import pandas as pd

# Membuat Series dari Dictionary
users = {
    "aku1": {"password": "123456"},
    "Koko": {"password": "admin123"},
    "admin": {"password": "admin#1234"}
}
result1 = pd.Series(users)

# Membuat DataFrame dari Tuple
events = (
    ("Interstellar", "Drama", "2024-10-01 19:00"),
    ("Barbie", "Pop", "2024-10-05 20:00"),
    ("The Raid", "Action", "2024-10-10 18:30")
)
result2 = pd.DataFrame(events, columns=["judul", "genre", "tanggal"])

# 1. Membaca Data dengan Pandas
# CSV
  # Menyimpan ke file
events_df = pd.read_csv(r'Modul5\Codelab\events.csv')  # Membaca kembali dari file
print("Data yang dibaca dari file CSV:")
print(events_df)

# 2. Operasi Dasar pada DataFrame
# Menampilkan informasi data
print("\nInformasi DataFrame:")
print(events_df.info())

# Menampilkan deskripsi statistik dari kolom data
print("\nDeskripsi Statistik DataFrame:")
print(events_df.describe(include='all'))

# Filter data berdasarkan genre
print("\nFilter data dengan genre 'Drama':")
filtered_data = events_df[events_df["genre"] == "Drama"]
print(filtered_data)

# Menambahkan kolom baru untuk tahun
events_df["tahun"] = pd.to_datetime(events_df["tanggal"]).dt.year
print("\nDataFrame dengan kolom tahun:")
print(events_df)

# Menyortir data berdasarkan tanggal
sorted_events = events_df.sort_values("tanggal")
print("\nDataFrame setelah diurutkan berdasarkan tanggal:")
print(sorted_events)

# Menampilkan hasil awal
print("\nSeries:")
print(result1)
print("\nDataFrame:")
print(result2)
