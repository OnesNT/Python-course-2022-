a = int(input())
str1 = str(input())

print(str1[0:a])
str1 = str1[a:]
while len(str1) > 0:
    for i in range(0, a-1):
        print('&', end ='')
    first_alpha = str1[0]
    if first_alpha != ' ':
        print(first_alpha)
    else:
        print()
    str1 = str1[1:]