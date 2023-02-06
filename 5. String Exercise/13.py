def separate_by_hyphens(s1):
    for ch in s1:
        if ch == '-':
            print('\n')
        else:
            print(ch, end='')
    return ''


str1 = 'Emma-is-a-data-scientist'
print(separate_by_hyphens(str1))