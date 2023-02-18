def unique_values(s_dict):
    s_set = list(set(s_dict.values()))
    return s_set


speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
print(unique_values(speed))
