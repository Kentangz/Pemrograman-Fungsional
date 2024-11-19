import time
import math

# Dekorator untuk menghitung waktu eksekusi
def hitung_waktu(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Waktu eksekusi: {end_time - start_time} detik")
        return result
    return wrapper

# Fungsi untuk translasi
def translasi(tx, ty):
    def transformasi(point):
        x, y = point
        return (x + tx, y + ty)
    return transformasi

# Fungsi untuk rotasi
def rotasi(theta):
    def transformasi(point):
        x, y = point
        rad = math.radians(theta)
        x_rot = x * math.cos(rad) - y * math.sin(rad)
        y_rot = x * math.sin(rad) + y * math.cos(rad)
        return (x_rot, y_rot)
    return transformasi

# Fungsi untuk dilatasi
def dilatasi(faktor_skala):
    def transformasi(point):
        x, y = point
        return (x * faktor_skala, y * faktor_skala)
    return transformasi

# Fungsi untuk input dan pemetaan titik
@hitung_waktu
def input_to_points(input_string):
    numbers = list(map(int, input_string.split(',')))
    if len(numbers) % 2 != 0:
        raise ValueError("Jumlah angka harus genap untuk membentuk titik-titik.")
    points = [(numbers[i], numbers[i+1]) for i in range(0, len(numbers), 2)]
    return points

# Fungsi untuk melakukan transformasi
@hitung_waktu
def lakukan_transformasi(points):
    translasi_fungsi = translasi(3, 7)
    points = [translasi_fungsi(point) for point in points]
    print("Setelah translasi:", points)
    
    rotasi_fungsi = rotasi(60)
    points = [rotasi_fungsi(point) for point in points]
    print("Setelah rotasi:", points)
    
    dilatasi_fungsi = dilatasi(1.5)
    points = [dilatasi_fungsi(point) for point in points]
    print("Setelah dilatasi:", points)
    return points

# Program utama langsung
input_string = input("Masukkan angka yang dipisahkan koma: ")
try:
    points = input_to_points(input_string)
    print("Titik-titik:", points)
    lakukan_transformasi(points)
except ValueError as e:
    print(e)
