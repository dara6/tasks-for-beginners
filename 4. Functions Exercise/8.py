def generate():
    for i in range(4, 31):
        a = []
        if i % 2 != 0:
            continue

        else:
            a.append(i)

    return a
print(generate())


