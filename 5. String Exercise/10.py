def count_same_symbols(str):
    ch_dict = dict()
    for ch in str:
        count = str.count(ch)
        ch_dict[ch] = count
    print(f'Result is: {ch_dict}')
    return ''


str1 = "Apple"
print(count_same_symbols(str1))
