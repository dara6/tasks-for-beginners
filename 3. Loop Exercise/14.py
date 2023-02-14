num = int(input("Enter a number: "))
result = 0
while num != 0:
    result = result * 10 + (num % 10)
    num //= 10
print(result)
