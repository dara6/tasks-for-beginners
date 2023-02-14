current = 0
next = 1
print("Fibbonacci sequence: ")
for i in range(10):
    print(current)
    current, next = next, current + next
