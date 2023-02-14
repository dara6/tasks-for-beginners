str1 = "P@#yn26at^&i5ve"

k_ch = 0
k_d = 0
k_s = 0
for ch in str1:
    if ch.isalpha():
        k_ch += 1
    elif ch.isdigit():
        k_d += 1
    else:
        k_s += 1

print(
    f"Total counts of chars, digits, and symbols\nChars = {k_ch}\nDigits = {k_d}\nSymbol = {k_s}"
)
