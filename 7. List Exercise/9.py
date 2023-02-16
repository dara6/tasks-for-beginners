def replace_20_200(list1):
    index = list1.index(20)
    list1[index] = 200
    return list1


test_list = [5, 10, 15, 20, 25, 50, 20]
print(replace_20_200(test_list))
