from datetime import datetime

# Data penjualan dengan 4 tanggal berbeda, setiap tanggal 3 produk
data_penjualan = [
    {"id": "GN101", "nama": "Topi", "harga": 50000, "quantity": 5, "tanggal": "2024-10-01"},
    {"id": "GN102", "nama": "Masker", "harga": 150000, "quantity": 2, "tanggal": "2024-10-01"},
    {"id": "GN103", "nama": "Headset", "harga": 100000, "quantity": 3, "tanggal": "2024-10-01"},
    {"id": "GN104", "nama": "Kalung", "harga": 200000, "quantity": 1, "tanggal": "2024-10-02"},
    {"id": "GN105", "nama": "Baju", "harga": 75000, "quantity": 4, "tanggal": "2024-10-02"},
    {"id": "GN106", "nama": "Jaket", "harga": 120000, "quantity": 2, "tanggal": "2024-10-02"},
    {"id": "GN107", "nama": "Gelang", "harga": 90000, "quantity": 6, "tanggal": "2024-10-03"},
    {"id": "GN108", "nama": "Celana", "harga": 130000, "quantity": 1, "tanggal": "2024-10-03"},
    {"id": "GN109", "nama": "Sabuk", "harga": 45000, "quantity": 8, "tanggal": "2024-10-03"},
    {"id": "GN110", "nama": "Sendal", "harga": 30000, "quantity": 10, "tanggal": "2024-10-04"},
    {"id": "GN111", "nama": "Kaos Kaki", "harga": 85000, "quantity": 3, "tanggal": "2024-10-04"},
    {"id": "GN112", "nama": "Sepatu", "harga": 200000, "quantity": 1, "tanggal": "2024-10-04"},
]

def hitung_pendapatan(data):
    hasil = []
    for item in data:
        hasil.append({
            "id": item["id"],
            "nama": item["nama"],
            "harga": item["harga"],
            "quantity": item["quantity"],
            "tanggal": item["tanggal"],
            "total_pendapatan": item["harga"] * item["quantity"]
        })
    return hasil

# Fungsi untuk menampilkan output dengan format yang rapi
def tampilkan_data_penjualan(pendapatan):
    for item in pendapatan:
        print(f"Produk ID  : {item['id']}")
        print(f"Nama Produk: {item['nama']}")
        print(f"Harga      : {item['harga']}")
        print(f"Jumlah     : {item['quantity']}")
        print(f"Tanggal    : {item['tanggal']}")
        print(f"Total Pendapatan: {item['total_pendapatan']}\n")
        print("="*40)

pendapatan = hitung_pendapatan(data_penjualan)
tampilkan_data_penjualan(pendapatan)

def total_penjualan(data):
    # Menghitung total penjualan per tanggal
    total_per_tanggal = {}
    for item in data:
        tanggal = item['tanggal']
        total = item['total_pendapatan']
        if tanggal in total_per_tanggal:
            total_per_tanggal[tanggal] += total
        else:
            total_per_tanggal[tanggal] = total

    for tanggal, total in total_per_tanggal.items():
        yield f"Tanggal: {tanggal}, Total Penjualan: {total}"

for hasil in total_penjualan(pendapatan):
    print(hasil)

def average_penjualan(data):
    try:
        # Meminta input tanggal dari pengguna
        tanggal_input = input("\nMasukkan tanggal penjualan (format: YYYY-MM-DD): ")
        datetime.strptime(tanggal_input, "%Y-%m-%d")

        penjualan_per_tanggal = [item for item in data if item["tanggal"] == tanggal_input]

        if not penjualan_per_tanggal:
            raise ValueError("Tanggal tidak ditemukan dalam data penjualan.")

        total_pendapatan = sum(item["harga"] * item["quantity"] for item in penjualan_per_tanggal)
        total_unit_terjual = sum(item["quantity"] for item in penjualan_per_tanggal)

        rata_rata = int(total_pendapatan / total_unit_terjual)

        # Menampilkan hasil
        print(f"\nRata-rata penjualan pada tanggal {tanggal_input} adalah Rp.{rata_rata}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

average_penjualan(data_penjualan)
