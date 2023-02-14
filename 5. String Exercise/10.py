def count_same_symbols(str):
    ch_dict = dict()
    for ch in str:
        ch_dict[ch] = ch_dict.get(ch, 0) + 1
    return ch_dict


str1 = "Apple"
print(count_same_symbols(str1))
