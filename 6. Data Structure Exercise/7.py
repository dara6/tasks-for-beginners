def is_subset(set1, set2):
    return set1 <= set2


first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
print(is_subset(first_set, second_set), is_subset(second_set, first_set))
