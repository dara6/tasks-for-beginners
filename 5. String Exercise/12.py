def find_last(s1, s2):
    for i in range(len(s1) - 1):
        if s1[i] == s2[0]:
            index = i
    return index


str1 = "Emma is a data scientist who knows Python. Emma works at google."
str2 = "Emma"
print(find_last(str1, str2))