def outer_func(a, b):
    def inner_func(a, b):
        return a + b
    addition = inner_func(a, b)
    return addition + 5


print(outer_func(10, 20))
