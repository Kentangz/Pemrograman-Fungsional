def bank_account(initial_balance):
    balance = initial_balance  # Variabel saldo di lingkup luar yang disimpan oleh closure
    
    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount
            return f"Added {amount}. New balance: {balance}"
        return "Invalid deposit amount."
    
    def get_balance():
        return f"Current balance: {balance}"
    
    # Mengembalikan kedua fungsi closure untuk akses saldo
    return deposit, get_balance

# Membuat rekening baru dengan saldo awal
deposit_function, get_balance_function = bank_account(1000)

# Pemanggilan fungsi untuk deposit dan melihat saldo
print(get_balance_function())  # Output: Current balance: 1000
print(deposit_function(500))   # Output: Added 500. New balance: 1500
print(get_balance_function())  # Output: Current balance: 1500
print(deposit_function(-200))  # Output: Invalid deposit amount.
