import test
a = int(input())
i = 1
num = 333
while i < a:
    num += 1
    num_str = str(num)
    if num_str.count('3') == 3:
        i += 1
print(num)
print(test.res(a-1))
