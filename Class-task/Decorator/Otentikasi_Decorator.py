# Decorator untuk memeriksa izin akses
def auth_decorator(func):
    def wrapper(user, *args, **kwargs):
        if user.get("is_authenticated"):
            print(f"Access granted for user: {user['name']}")
            return func(*args, **kwargs)
        else:
            print("Access denied. User not authenticated.")
    return wrapper

# Fungsi yang memerlukan otentikasi
@auth_decorator
def view_sensitive_data():
    print("Accessing sensitive data...")

# Contoh pengguna
user1 = {"name": "Alice", "is_authenticated": True}
user2 = {"name": "Bob", "is_authenticated": False}

# Pemanggilan fungsi dengan dekorator otentikasi
view_sensitive_data(user1)  # User yang sudah terautentikasi
view_sensitive_data(user2)  # User yang belum terautentikasi
