def make_dict(list):
    list_dict = dict()
    for l in list:
        if l in list_dict:
            list_dict[l] += 1
        else:
            list_dict[l] = 1
    print(list_dict)


sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(make_dict(sample_list))