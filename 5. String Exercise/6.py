def func(str1, str2):
    result = ""
    reversed_str2 = str2[::-1]
    for i in range(0, len(str1)):
        result += str1[i] + reversed_str2[i]
    return result


s1 = "Abc"
s2 = "Xyz"
print(func(s1, s2))
