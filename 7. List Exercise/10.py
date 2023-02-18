def remote_20(list1):
    res = []
    for l in list1:
        if l != 20:
            res.append(l)
    return res


test_list = [5, 20, 15, 20, 25, 50, 20]
print(remote_20(test_list))