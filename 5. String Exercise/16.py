def remove_ch_str(str):
    res_str = ""
    for s in str:
        if s.isdigit():
            res_str += s
    return res_str


str1 = "I am 25 years and 10 months old"
print(remove_ch_str(str1))
