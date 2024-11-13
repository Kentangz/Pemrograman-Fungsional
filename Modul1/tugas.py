users = {
    "Aku1": {"password": "123"},
    "Koko96": {"password": "admin123"},
    "admin": {"password": "admin#1234"}
}

events = (
    ("Interstellar", "Drama", "2024-10-01 19:00"),
    ("Barbie", "Pop", "2024-10-05 20:00"),
    ("The Raid", "Action", "2024-10-10 18:30")
)

bookings = {
    "Aku1": [
        {"event": events[0], "name": "gwehj"},
        {"event": events[2], "name": "luwh"}
    ]
}

def register():
    id = input("Masukkan id: ")
    if id in users:
        print("id sudah terdaftar. Silakan login.")
        return

    password = input("Masukkan password: ")
    users[id] = {'password': password}
    bookings[id] = []  # bookinglist

    print("Registrasi berhasil! Sekarang Anda bisa login.")

def login():
    id = input("Masukkan id: ")
    if id not in users:
        print("id belum terdaftar. Silakan register terlebih dahulu.")
        return None

    password = input("Masukkan password: ")
    if users[id]['password'] == password:
        print("Login berhasil!")
        return id
    else:
        print("Password salah.")
        return None

def view_events():
    print("\n--- Daftar Film/Konser ---")
    for index, event in enumerate(events):
        print(f"{index + 1}. Judul: {event[0]}, Genre: {event[1]}, Waktu: {event[2]}")

def book_ticket(id):
    view_events()
    try:
        choice = int(input("Pilih nomor event untuk booking (1-3): ")) - 1
        if choice < 0 or choice >= len(events):
            print("Pilihan tidak valid.")
            return

        name = input("Masukkan nama pemesan: ")
        if not name:
            print("Nama pemesan tidak boleh kosong.")
            return

        booking = {
            "event": events[choice],
            "name": name
        }

        bookings[id].append(booking)
        print("Booking tiket berhasil!")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def view_bookings(id):
    print("\n--- Daftar Booking Anda ---")
    if not bookings[id]:
        print("Anda belum melakukan booking.")
        return

    for index, booking in enumerate(bookings[id]):
        event = booking["event"]
        print(f"{index + 1}. Event: {event[0]}, Pemesan: {booking['name']}")

def delete_booking(id):
    view_bookings(id)
    try:
        choice = int(input("Pilih nomor booking untuk dihapus: ")) - 1
        if choice < 0 or choice >= len(bookings[id]):
            print("Pilihan tidak valid.")
            return

        bookings[id].pop(choice)
        print("Booking berhasil dihapus.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def edit_event():
    global events
    view_events()
    try:
        choice = int(input("Pilih nomor event untuk diedit (1-3): ")) - 1
        if choice < 0 or choice >= len(events):
            print("Pilihan tidak valid.")
            return

        title = input("Masukkan judul baru: ")
        genre = input("Masukkan genre baru: ")
        time = input("Masukkan waktu baru (YYYY-MM-DD HH:MM): ")

        events = list(events)
        events[choice] = (title, genre, time)
        events = tuple(events)

        print("Event berhasil diperbarui.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def add_event():
    global events
    title = input("Masukkan judul event baru: ")
    genre = input("Masukkan genre event baru: ")
    time = input("Masukkan waktu event baru (YYYY-MM-DD HH:MM): ")

    new_event = (title, genre, time)
    events = list(events)
    events.append(new_event)
    events = tuple(events)

    print("Event baru berhasil ditambahkan.")

def admin_menu():
    while True:
        print("\n--- Menu Admin ---")
        print("1. Lihat Daftar Event")
        print("2. Edit Event")
        print("3. Tambah Event")
        print("4. Logout")

        admin_choice = input("Pilih menu: ")

        if admin_choice == "1":
            view_events()
        elif admin_choice == "2":
            edit_event()
        elif admin_choice == "3":
            add_event()

        elif admin_choice == "4":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")

def main():
    while True:
        print("\n--- Sistem Booking Tiket ---")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            register()
        elif choice == "2":
            id = login()
            if id:
                if id == "admin":  # Jika admin login
                    admin_menu()
                else:  # Jika pengguna biasa login
                    while True:
                        print("\n--- Menu Pengguna ---")
                        print("1. Lihat Daftar Event")
                        print("2. Booking Tiket")
                        print("3. Lihat Booking")
                        print("4. Hapus Booking")
                        print("5. Logout")

                        user_choice = input("Pilih menu: ")

                        if user_choice == "1":
                            view_events()
                        elif user_choice == "2":
                            book_ticket(id)
                        elif user_choice == "3":
                            view_bookings(id)
                        elif user_choice == "4":
                            delete_booking(id)
                        elif user_choice == "5":
                            print("Logout berhasil.")
                            break
                        else:
                            print("Pilihan tidak valid.")
        elif choice == "3":
            print("Terima kasih! Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid.")

# Jalankan aplikasi
main()
