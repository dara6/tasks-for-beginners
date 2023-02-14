str = "PYnAtivE"
list1 = []
list2 = []
for ch in str:
    if ch.islower():
        list1.append(ch)
    else:
        list2.append(ch)

new_str = "".join(list1 + list2)
print(new_str)
