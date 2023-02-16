def add_list_to_list(l, s_l):
    l[2][1][2].extend(s_l)
    return l


test_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
print(add_list_to_list(test_list, sub_list))