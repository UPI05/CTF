chrs = [16, 9, 3, 15, 3, 20, 6, -1, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, -2]

res = ""

for c in chrs:
    if c == -1:
        res += "{"
    elif c == -2:
        res += "}"
    else:
        res += chr(ord('a') - 1 + c)

print(res)