a = int(input())
b = int(input())

if a == 0:
    print("False")
else:
    check_res = True
    if int(a & b) > 0:
        check_res = False
    print(check_res)

