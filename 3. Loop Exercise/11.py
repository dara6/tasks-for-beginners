start = 25
end = 50
for i in range(start, end + 1):
    if i == 2:
        print(i)
    elif i < 10 and i % 2 != 0 and i % 3 != 0:
        print(i)
    elif i > 10 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print(i)
    else:
        continue