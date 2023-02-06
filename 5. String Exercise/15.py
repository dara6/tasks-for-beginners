def remove_punc_symb(str):
    new_str = ""
    res_str = ""
    for s in str:
        if s.isalpha() or s == ' ':
            new_str += s
    for i in range(0, len(new_str)):
        if new_str[i - 1] == new_str[i] == ' ':
            continue
        else:
            res_str += new_str[i]
    print(res_str)
    return ''


str1 = "/*Jon is @developer & musician"
print(remove_punc_symb(str1))