
str = input()
res = ""

lowercase = str[0 : len(str) : 2].lower()
uppercase = str[1 : len(str) : 2].upper()

for i in range(len(str)):
    if i % 2 == 0:
        res += lowercase[int(i / 2)]
    else:
        res += uppercase[int((i - 1) / 2)]

print(res)