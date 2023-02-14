def func(str1, str2):
    res = ''
    for i in range(0, len(str1) // 2):
        res += str1[i]
    for j in range(0, len(str2)):
        res += str2[j]
    for k in range(len(str1) // 2, len(str1)):
        res += str1[k]
    print(res)

    return ''

s1 = "Ault"
s2 = "Kelly"
print(func(s1, s2))