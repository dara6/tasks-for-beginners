def str_decreaser(str):
    for i in range(0, len(str) + 1):
        if i == (len(str) // 2 - 1) or i == (len(str) // 2) or i == (len(str) // 2 + 1):
            print(str[i], end='')
        else:
            continue
    return ''
str1 = 'James'
print(str_decreaser(str1))