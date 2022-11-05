
n = int(input())
k = int(input())
dict_wires = dict()
if k == 0 or n == 0:
    print()
else:
    for i in range(n):
        list_wires = set(str(input()).split(' '));
        # if ' ' in list_wires:
        #     list_wires.remove(' ');

        for j in list_wires:
            if j not in dict_wires:
                dict_wires.setdefault(j, 1)
            else:
                dict_wires[j] += 1;

    delete_num = set(str(input()).split(' '));
    for i in delete_num:
        if i in dict_wires:
            del dict_wires[i]

    arr_wires = sorted([i for i in dict_wires.values()])
    # print(*arr_wires[len(arr_wires) - k: len(arr_wires)])
    if len(arr_wires) >= k:
        for i in range(len(arr_wires) - k, len(arr_wires)):
            print(arr_wires[i])
    else:
        for i in range(len(arr_wires)):
            print(arr_wires[i])
