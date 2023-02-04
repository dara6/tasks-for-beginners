for i in range(1, 11):
    if i < 6:
        print('* ' * i)
    else:
        for j in range(6):
            print('* ' * (i - j))
        break