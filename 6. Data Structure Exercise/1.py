def make_l3(list1, list2):
    l1 = list1[1::2]
    l2 = list2[0::2]
    l3 = l1 + l2
    print(f'Element at odd-index positions from list one {l1}\nElement at even-index positions from list one {l2}\nResult is: {l3}')
    return ''


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
print(make_l3(l1, l2))