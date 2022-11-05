# f = open("input.txt", "r")
# mess = ''
# for line in f:
#     mess += line[:len(line) - 1] + '@ '
# f.close()
#
# f = open("output.txt", "a")
# list_mess = mess.split()
#
#
# # mess = input()
# # list_mess = mess.split()
#
# def check_if_interseting(string):
#     if string[0] == '.':
#         return False
#
#     for char in string:
#         if not (char.isdigit() or char.islower() or char == '.' or char == '@'):
#             return False
#     return True
#
# # print(list_mess)
# for string in list_mess:
#     if check_if_interseting(string) and (string.endswith(".hlm") or string.endswith(".hlm@") or string.endswith(".brhl@") or string.endswith(".hlm.@")  or string.endswith(".brhl.@") or string.endswith('.hlm..@') or string.endswith('.brhl..@')):
#         if string.endswith('.hlm.@') or string.endswith('.brhl.@') or string.endswith('.hlm..@') or string.endswith('.brhl..@'):
#             f.write(string[:len(string) - 2])
#             f.write('\n')
#         elif string.endswith('.hlm@') or string.endswith('.brhl@'):
#                 f.write(string[:len(string) - 1])
#                 f.write('\n')
#         else:
#             f.write(string)
#             f.write('\n')
#         # print(string)
# f.close()

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