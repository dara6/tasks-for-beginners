def find_name_with_digits(str):
    res = []
    new_str = str.split()
    for item in new_str:
        if any(char.isalpha() for char in item) and any(
            char.isdigit() for char in item
        ):
            res.append(item)
    print("The original string is : " + str1)
    print("Displaying words with alphabets and numbers")
    for i in res:
        print(i)
    return ""


str1 = "Emma25 is Data scientist50 and AI Expert"
print(find_name_with_digits(str1))
