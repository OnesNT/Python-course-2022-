f = open("input.txt", "r")
password = f.readline()

def count_num(string):
    temp = 0
    for char in string:
        if char >= '0' and char <= '9':
            temp += 1
    return temp


def contains_lower(string):
    return any(char.islower() for char in string)

def contains_upper(string):
    return any(char.isupper() for char in string)

f.close()
f = open("output.txt", "a")

if count_num(password) > 0 and contains_upper(password) and contains_lower(password):
    f.write('YES')
else:
    f.write('NO')

f.write('\n')

if len(password) <= 10 and count_num(password) <= 3:
    f.write('YES')
else:
    f.write('NO')

f.close()