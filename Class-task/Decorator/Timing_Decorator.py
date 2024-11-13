import time

# Decorator untuk mengukur waktu eksekusi
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Catat waktu mulai
        result = func(*args, **kwargs)  # Jalankan fungsi asli
        end_time = time.time()  # Catat waktu selesai
        execution_time = end_time - start_time  # Hitung waktu eksekusi
        print(f"Function '{func.__name__}' executed in: {execution_time:.4f} seconds")
        return result
    return wrapper

# Fungsi yang akan diukur waktu eksekusinya
@timing_decorator
def process_data(data):
    time.sleep(2)  # Simulasi proses yang memakan waktu
    print("Processing data...")
    return f"Processed {len(data)} items."

# Pemanggilan fungsi
data = [i for i in range(1000)]  # Data untuk diproses
process_data(data)
