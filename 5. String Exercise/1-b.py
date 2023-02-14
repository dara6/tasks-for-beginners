def str_decreaser(string):
    mid = len(string) // 2
    result = string[mid - 1 : mid + 2]
    return result


str1 = "James"
print(str_decreaser(str1))
