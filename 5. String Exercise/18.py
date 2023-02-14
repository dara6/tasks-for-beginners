def remove_punc_symb(str):
    res_str = ""
    for s in str:
        if s.isalpha() or s == " ":
            res_str += s
        else:
            res_str += "#"
    print(res_str)
    return ""


str1 = "/*Jon is @developer & musician"
print(remove_punc_symb(str1))
