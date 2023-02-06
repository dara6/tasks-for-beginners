def str_is_balanced(str1, str2):
    flag = True
    for ch in str1:
        if ch in str2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
flag = str_is_balanced(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = str_is_balanced(s1, s2)
print("s1 and s2 are balanced:", flag)

