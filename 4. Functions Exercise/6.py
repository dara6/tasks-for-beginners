def recursive_func(number):
    if number > 0:
        return number + recursive_func(number - 1)
    else:
        return 0


print(recursive_func(10))
