def concatenate(l1, l2):
    list3 = []
    for i in range(0, len(l1)):
        for j in range(0, len(l2)):
            l3 = l1[i] + l2[j]
            list3.append(l3)
    return list3


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
print(concatenate(list1, list2))
