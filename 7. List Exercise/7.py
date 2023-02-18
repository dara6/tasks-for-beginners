def include_item(list1):
    item = 7000
    list1[2][2].append(item)
    return list1


test_list = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print(include_item(test_list))
