a = int(input())
b = int(input())

str1_list = []
check_len = 0
list_check = [0]
count = 0
check_sliding = [0]

while True:
    st = str(input())
    if st == '0':
        break
    if list_check[- 1] + len(st) > a or count >= b:
        check_len = len(st) + 1
        count = 1
        check_sliding.append(len(list_check) - 1)
    else:
        check_len += len(st) + 1
        count += 1
    list_check.append(check_len)
    str1_list.append(st)

check_sliding.append(len(str1_list))
for i in range(0, len(check_sliding) - 1):
    print(*str1_list[check_sliding[i] : check_sliding[i + 1]])
