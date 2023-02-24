def func(s_dict, a):
    return a in s_dict.values()

sample_dict = {'a': 100, 'b': 200, 'c': 300}
print(func(sample_dict, 200))