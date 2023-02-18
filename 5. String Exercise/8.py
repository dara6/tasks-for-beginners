def find_substr(s1, s2):
    new_s1 = s1.lower()
    count = new_s1.count(s2.lower())
    return count


str1 = "Welcome to USA. usa awesome, isn't it?"
str2 = "USA"
print("The USA count is:", find_substr(str1, str2))
