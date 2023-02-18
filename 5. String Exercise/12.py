def find_last(s1, s2):
    index = s1.rfind(s2)
    return index


str1 = "Emma is a data scientist who knows Python. Emma works at google."
str2 = "Emma"
print(find_last(str1, str2))
