def make_new_list(s_list):
    new_s_list = []
    for s in s_list:
        if s:
            new_s_list.append(s)
    print(f'Original list of sting {s_list}\nAfter removing empty strings {new_s_list}')
    return ''


str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print(make_new_list(str_list))

