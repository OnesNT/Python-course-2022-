a = int(input())
b = int(input())

for i in range(a):
    for j in range(b):
        if j < b - 1:
            print('*   *', end = ' ')
        else:
            print('*   *')
    for j in range(b):
        if j < b - 1:
            print('*  **', end = ' ')
        else:
            print('*  **')
    for j in range(b):
        if j < b - 1:
            print('* * *', end = ' ')
        else:
            print('* * *')
    for j in range(b):
        if j < b - 1:
            print('**  *', end = ' ')
        else:
            print('**  *')
    for j in range(b):
        if j < b - 1:
            print('*   *', end = ' ')
        else:
            print('*   *')
    print()