def reverse(str):
    for i in range(len(str) - 1, 0, -1):
        print(str[i], end='')
    return ''


str1 = "PYnative"
print(reverse(str1))
