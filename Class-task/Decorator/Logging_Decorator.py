def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is about to run")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' has completed")
        return result
    return wrapper

@log_decorator
def greet(name):
    print(f"Hello, {name}!")

# Pemanggilan fungsi
greet("Alice")
