def find_largest(x):
    res = x[0]
    for i in range(1, len(x)):
        if x[i] > res:
            res = x[i]
    return res

x = [1, 10, 2, 3]
print(find_largest(x))
