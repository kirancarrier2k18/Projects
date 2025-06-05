

def add(a, b):
    print("Addition:", a + b)

# Decorator that adds multiplication
def smart_decorator(func):
    def wrapper(a, b):
        print("Multiplication:", a * b)
        func(a, b)  # Call the original function
    return wrapper

# Apply the decorator
#add = smart_decorator(add)

# Call the decorated function
add(4, 2)