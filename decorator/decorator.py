def decorator(func):
    def inner():
        print("function has been decorated.")
        func()
    return inner

@decorator
def simple_func():
    print("This is simple function.")

simple_func()