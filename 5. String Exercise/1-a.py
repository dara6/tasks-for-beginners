def str_decreaser(string):
    length = len(string)
    result = "{}{}{}".format(string[0], string[length // 2], string[length - 1])
    return result


str1 = "James"
print(str_decreaser(str1))
