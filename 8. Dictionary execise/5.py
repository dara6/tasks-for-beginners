sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

dict1 = {k: sample_dict[k] for k in keys if k in sample_dict}
print(dict1)
