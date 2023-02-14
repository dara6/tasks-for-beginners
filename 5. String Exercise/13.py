def separate_by_hyphens(s1):
    result = '\n'.join(s1.split('-'))
    return result


str1 = "Emma-is-a-data-scientist"
print(separate_by_hyphens(str1))
