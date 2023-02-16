def make_square(list1):
    list2 = []
    for l in list1:
        list2.append(l * l)
    return list2


test_list = [1, 2, 3, 4, 5, 6, 7]
print(make_square(test_list))