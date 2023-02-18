def solution(r_number, s_dict):
    s_dict_values_set = set(s_dict.values())
    for num in r_number.copy():
        if num not in s_dict_values_set:
            r_number.remove(num)


roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
print(solution(roll_number, sample_dict), roll_number)
