def decorator(func):
    def inner(list_of_names):
        return [func(name) for name in list_of_names]
    return inner


@decorator
def camelcase(s):
    return s.capitalize()


names = ['first', 'second', 'third']
print(camelcase(names))