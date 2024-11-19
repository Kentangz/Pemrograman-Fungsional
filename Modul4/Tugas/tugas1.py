from datetime import datetime

# Data awal
initial_users = {
    "aku1": {"password": "123456"},
    "Koko": {"password": "admin123"},
    "admin": {"password": "admin#1234"}
}

initial_events = (
    ("Interstellar", "Drama", "2024-10-01 19:00"),
    ("Barbie", "Pop", "2024-10-05 20:00"),
    ("The Raid", "Action", "2024-10-10 18:30")
)

# Decorator untuk validasi input
def validate_register(func):
    def wrapper(users, username, password):
        if len(password) < 6:
            raise ValueError("Password harus memiliki minimal 6 karakter.")
        if username in users:
            raise ValueError("ID sudah terdaftar. Silakan login.")
        return func(users, username, password)
    return wrapper

def validate_booking(func):
    def wrapper(bookings, username, event_index, name):
        if event_index < 0 or event_index >= len(initial_events):
            raise IndexError("Pilihan event tidak valid.")
        if not name.strip():
            raise ValueError("Nama pemesan tidak boleh kosong.")
        return func(bookings, username, event_index, name)
    return wrapper

# Fungsi untuk register user dengan validasi
@validate_register
def register_user(users, username, password):
    return {**users, username: {"password": password}}

# Fungsi untuk booking tiket dengan validasi
@validate_booking
def book_ticket(bookings, username, event_index, name):
    if username not in bookings:
        bookings[username] = []
    bookings[username].append({"event": initial_events[event_index], "name": name})
    return bookings

# Closure untuk mendapatkan event tertentu berdasarkan waktu
def filter_events_by_time(target_time):
    def filter_func(events):
        return [event for event in events if event[2] >= target_time]
    return filter_func

#
def display_events(events, formatter):
    return list(map(formatter, events))

# Testing
users = initial_users
bookings = {}

# Register user dengan password valid
try:
    users = register_user(users, "Andi", "passsss")
    print("Registrasi berhasil. Users sekarang:", users)
except ValueError as e:
    print(f"Error saat registrasi: {e}")

# Register user dengan password tidak valid
try:
    users = register_user(users, "Alek", "pas")
except ValueError as e:
    print(f"Error saat registrasi: {e}")

# Booking tiket dengan nama kosong
try:
    bookings = book_ticket(bookings, "coki", 1, " ")
except ValueError as e:
    print(f"Error saat booking: {e}")

# Booking tiket valid
try:
    bookings = book_ticket(bookings, "NewUser", 1, "Alice")
    print("Booking berhasil. Daftar booking sekarang:", bookings)
except ValueError as e:
    print(f"Error saat booking: {e}")

# Filter events setelah waktu tertentu
filter_future_events = filter_events_by_time("2024-10-05")
filtered_events = filter_future_events(initial_events)
print("\nEvent setelah 2024-10-05:")
for event in filtered_events:
    print(event)

# Tampilkan semua event dengan format khusus
formatted_events = display_events(
    initial_events, lambda e: f"Judul: {e[0]}, Genre: {e[1]}, Waktu: {e[2]}"
)
print("\nDaftar Event yang Ditampilkan:")
for event in formatted_events:
    print(event)