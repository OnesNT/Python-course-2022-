st1 = 'manul'
st2 = 'massiv'
st3 = 'hahaha'

st = input()
check_exist = 0

if (st1 in st):
    check_exist += 1
if (st2 in st):
    check_exist += 1
if (st3 in st):
    check_exist += 1

if (check_exist == 2):
    print('True')
else :
    print ('False')