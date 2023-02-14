def sum_and_average(str):
    count = 0
    sum = 0
    for ch in str:
        if ch.isdigit():
            sum += int(ch)
            count += 1
    print(f'Sum is: {sum} Average is: {sum / count}')
    return ''


str1 = "PYnative29@#8496"
print(sum_and_average(str1))

