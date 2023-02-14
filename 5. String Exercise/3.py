def str_decreaser(str1, str2):
    res = ""
    res += (
        str1[0]
        + str2[0]
        + str1[len(str1) // 2]
        + str2[len(str2) // 2]
        + str1[len(str1) - 1]
        + str2[len(str2) - 1]
    )
    return res


s1 = "America"
s2 = "Japan"

print(str_decreaser(s1, s2))
