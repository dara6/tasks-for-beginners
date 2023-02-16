def remote_empty(list1):
    res =[]
    for l in list1:
        if l != "":
            res.append(l)
    return res


test_list = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(remote_empty(test_list))