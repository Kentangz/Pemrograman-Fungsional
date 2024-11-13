def make_counter():
    count = 0  # Variabel di lingkup luar yang diingat oleh closure
    
    def increment():
        nonlocal count  # Akses variabel 'count' di lingkup luar
        count += 1
        return count
    
    return increment

# Membuat instance counter
counter_a = make_counter()
counter_b = make_counter()

# Pemanggilan fungsi untuk setiap counter
print(counter_a())  # Output: 1
print(counter_a())  # Output: 2
print(counter_b())  # Output: 1 (independen dari counter_a)
print(counter_b())  # Output: 2
print(counter_a())  # Output: 3
