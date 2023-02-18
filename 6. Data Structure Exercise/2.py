def remove(list):
    l = list.pop(4)
    print("List after removing element at index 4 ", list)
    list.insert(2, l)
    print("List after Adding element at index 2 ", list)
    list.insert(len(list) - 1, l)
    print("List after Adding element at last ", list)
    return ''

list1 = [34, 54, 67, 89, 11, 43, 94]
print(remove(list1))