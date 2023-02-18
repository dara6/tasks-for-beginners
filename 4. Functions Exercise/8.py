def generate(start, end):
    a = []
    for i in range(start, end + 1):
        if i % 2 != 0:
            continue
        else:
            a.append(i)
    return a


print(generate(4, 30))
