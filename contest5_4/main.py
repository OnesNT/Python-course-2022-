f1 = open("input.txt", "r")
f2 = open("output.txt", "a")
def check_if_interseting(string):
    if string[0] == '.':
        return False

    for char in string:
        if not (char.isdigit() or char.islower() or char == '.' ):
            return False

    return True


for line in f1:
    mess = line
    list_mess = mess.split()

    for string in list_mess:
        if check_if_interseting(string):
            if (string.endswith(".hlm") or string.endswith(".brhl")):
                f2.write(string[:len(string)])
                f2.write('\n')
            if (string.endswith(".hlm.") or string.endswith(".hlm..")  \
                or string.endswith(".brhl.") or string.endswith(".brhl..")):
                f2.write(string[:len(string) - 1])
                f2.write('\n')

f1.close()
f2.close()
