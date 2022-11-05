f = open("input.txt", "r")

for line in f:
    log = line
    in4 = log.split()
    res = ''
    # check if string is mess
    check = False
    # store mess
    position = 0

    for string in in4:
        if check:
            position = log.index(string)
            break
        if "@" in string:
            check = True

    for i in range(position, len(log)):
        if log[i] != '\n':
            res += log[i]
    print(in4[0][0:7], end= '')
    print("{:.>73}".format(res))

f.close()
