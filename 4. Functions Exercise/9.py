x = [4, 6, 8, 24, 12, 2]
def find_largest(x):
    for i in range(0, len(x) - 1):
        if x[i + 1] > x[i]:
            res = x[i + 1]
    print(res)

find_largest(x)
