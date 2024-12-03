import pandas as pd
file_path = 'Dataset Harga Buah dan Sayur.csv'
data = pd.read_csv(file_path)
print(f"=== 10 Data Pertama === \n {data.head(10)} \n \n")

# Ingformasi data
print("=== Informasi Data ===")
print(data.info())

# Mengonversi kolom tanggal menjadi tipe datetime
data['date'] = pd.to_datetime(data['date'])
data['year'] = data['date'].dt.year
# Menghitung rata-rata harga per tahun untuk setiap produk
average_price_per_year = data.groupby(['year', 'item'])['price'].mean().reset_index()
print(f" \n \nRata rata harga per tahun dari setiap produk \n {average_price_per_year}")

# Min max harga
highest_price = data.loc[data['price'].idxmax()]
lowest_price = data.loc[data['price'].idxmin()]
print("\nProduk dengan harga tertinggi:")
print(highest_price)
print("\nProduk dengan harga terendah:")
print(lowest_price)


# Memfilter produk dengan harga antara 1.50 dan 2.35
filtered_data = data[(data['price'] >= 1.50) & (data['price'] <= 2.35)]
print(f"\nProduk dengan Harga antara 1,50 dan 2,35 \n{filtered_data}")