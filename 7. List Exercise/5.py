def func(l1, l2):
    l2 = l2[::-1]
    for i in range(0, len(l1)):
        for j in range(0, len(l2)):
            if i == j:
                print(l1[i], l2[j])


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
print(func(list1, list2))
