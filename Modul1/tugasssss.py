from functools import reduce

# Data awal
initial_users = {
    "Aku1": {"password": "123"},
    "Koko96": {"password": "admin123"},
    "admin": {"password": "admin#1234"}
}

initial_events = (
    ("Interstellar", "Drama", "2024-10-01 19:00"),
    ("Barbie", "Pop", "2024-10-05 20:00"),
    ("The Raid", "Action", "2024-10-10 18:30")
)


def register_user(users, username, password):
    if username in users:
        raise ValueError("ID sudah terdaftar. Silakan login.")

    new_users = users.copy()
    new_users[username] = {"password": password}

    return new_users


# Fungsi untuk login
def login_user(users, username, password):
    if username not in users:
        raise ValueError("ID belum terdaftar. Silakan register terlebih dahulu.")

    if users[username]['password'] != password:
        raise ValueError("Password salah.")

    return username


# a
def get_events():
    return list(initial_events)


# Fungsi untuk menampilkan daftar acara
def display_events(events):
    print("\n--- Daftar Film/Konser ---")
    for index, event in enumerate(events, start=1):
        print(f"{index}. Judul: {event[0]}, Genre: {event[1]}, Waktu: {event[2]}")

def list_book():
    return list(initial_users.keys())

# Fungsi untuk memesan tiket
def book_ticket(bookings, username, event_index, name):
    if event_index < 0 or event_index >= len(initial_events):
        raise IndexError("Pilihan event tidak valid.")
    if not name:
        raise ValueError("Nama pemesan tidak boleh kosong.")

    new_bookings = bookings.copy()
    if username not in new_bookings:
        new_bookings[username] = []

    new_bookings[username].append({"event": initial_events[event_index], "name": name})

    return new_bookings



def view_bookings(bookings, username):
    return bookings.get(username, [])


# Fungsi untuk menghapus booking
def delete_booking(bookings, username, index):
    if username in bookings and 0 <= index < len(bookings[username]):
        new_bookings = bookings.copy()
        new_bookings[username].pop(index)
        return new_bookings
    else:
        raise IndexError("Pilihan tidak valid.")



def total_bookings(bookings, username):
    user_bookings = view_bookings(bookings, username)
    return reduce(count_booking, user_bookings, 0)


def count_booking(count, booking):
    return count + 11




def get_event_titles():
    return [event[0] for event in initial_events]



def filter_bookings_by_name(bookings, username, name):
    user_bookings = view_bookings(bookings, username)
    return filter_by_name(user_bookings, name)


def filter_by_name(bookings, name):
    return [booking for booking in bookings if booking['name'] == name]




def helper(user_bookings):
    if not user_bookings:
        return 0
    return 1 + count_bookings_recursive_helper(user_bookings[1])


# Fungsi untuk menjalankan menu utama
def main(users=initial_users, bookings={}):
    while True:
        print("\n--- Sistem Booking Tiket ---")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            username = input("Masukkan id: ")
            password = input("Masukkan password: ")
            try:
                users = register_user(users, username, password)
                print("Registrasi berhasil! Sekarang Anda bisa login.")
            except ValueError as ve:
                print(f"Error: {ve}")

        elif choice == "2":
            username = input("Masukkan id: ")
            password = input("Masukkan password: ")
            try:
                user_id = login_user(users, username, password)
                print("Login berhasil!")
                while True:
                    print("\n--- Menu Pengguna ---")
                    print("1. Lihat Daftar Event")
                    print("2. Booking Tiket")
                    print("3. Lihat Booking")
                    print("4. Hapus Booking")
                    print("5. ")
                    print("7")
                    print("6. Logout")

                    user_choice = input("Pilih menu: ")

                    if user_choice == "1":
                        display_events(get_events())
                    elif user_choice == "2":
                        display_events(get_events())
                        try:
                            event_index = int(input("Pilih nomor event untuk booking (1-3): ")) - 1
                            name = input("Masukkan nama pemesan: ")
                            bookings = book_ticket(bookings, user_id, event_index, name)
                            print("Booking tiket berhasil!")
                        except (ValueError, IndexError) as e:
                            print(f"Error: {e}")

                    elif user_choice == "3":
                        user_bookings = view_bookings(bookings, user_id)
                        if user_bookings:
                            print("\n--- Daftar Booking Anda ---")
                            for index, booking in enumerate(user_bookings):
                                event = booking["event"]
                                print(f"{index + 1}. Event: {event[0]}, Pemesan: {booking['name']}")
                        else:
                            print("Anda belum melakukan booking.")

                    elif user_choice == "4":
                        user_bookings = view_bookings(bookings, user_id)
                        if user_bookings:
                            try:
                                index = int(input("Pilih nomor booking untuk dihapus: ")) - 1
                                bookings = delete_booking(bookings, user_id, index)
                                print("Booking berhasil dihapus.")
                            except (ValueError, IndexError) as e:
                                print(f"Error: {e}")
                        else:
                            print("Anda belum melakukan booking.")

                    elif user_choice == "5":
                        total = total_bookings(bookings, user_id)
                        print(f"Total booking Anda: {total}")
                    elif user_choice == "7" :
                        filter_bookings_by_name(bookings, username, name)

                    elif user_choice == "6":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid.")
            except ValueError as ve:
                print(f"Error: {ve}")

        elif choice == "3":
            print("Terima kasih! Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid.")

# Jalankan aplikasi
main()
