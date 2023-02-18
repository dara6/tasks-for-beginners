def concatenate_two_lists(l1, l2):
    list3 = []
    for i in range(0, len(l1)):
        for j in range(0, len(l2)):
            if i == j:
                l3 = l1[i] + l2[j]
                list3.append(l3)
    return list3


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
print(concatenate_two_lists(list1, list2))
