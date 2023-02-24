def make_dict(emp, d):
    dict1 = dict()
    for e in emp:
        dict1[e] = d
    return dict1


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
print(make_dict(employees, defaults))
