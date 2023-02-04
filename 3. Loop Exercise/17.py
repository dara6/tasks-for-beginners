n = int(input("Enter a quantity of number: "))
num = 2
res = 0
for i in range(n):
    res += num
    num = num * 10 + 2
print(res)
