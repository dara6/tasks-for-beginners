import collections


def is_unique(s_list):
    return [i for i, j in collections.Counter(s_list).items() if j == 1]


sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
unique_list = is_unique(sample_list)
result_tuple = tuple(unique_list)
min_item = min(result_tuple)
max_item = max(result_tuple)
print(unique_list, result_tuple, min_item, max_item)
