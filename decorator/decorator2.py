def decorator(func):
    def inner(a, b):
        print("I am dividing %d with %d." % (a, b))
        if b == 0:
            print("Division by % d is not possible." % b)
            return
        return func(a, b)
    return inner

@decorator
def divide(a, b):
    return a/b

print(divide(20, 2))
print(divide(10, 0))