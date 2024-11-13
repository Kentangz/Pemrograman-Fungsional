import time

def schedule_task(task_name, delay):
    def execute_task():
        print(f"Tugas '{task_name}' dimulai...")
        time.sleep(delay)  # Simulasi delay
        print(f"Tugas '{task_name}' selesai setelah {delay} detik.")

    return execute_task  # Mengembalikan fungsi closure sebagai callback

# Membuat beberapa tugas terjadwal
task1 = schedule_task("Backup Database", 3)
task2 = schedule_task("Send Report", 5)

# Memulai tugas
task1()  # Output: Menjalankan tugas 'Backup Database'
task2()  # Output: Menjalankan tugas 'Send Report'
