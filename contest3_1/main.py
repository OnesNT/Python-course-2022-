


Roman_num = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI',
            'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX',
            'XXX']
A = [i for i in range(1, 31)]
Romann = dict(zip(Roman_num, A))

Greek_alpha = ('alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa')
B = [i for i in range(1, 11)]
Greek = dict(zip(Greek_alpha, B))

a = input()
check = True
st1 = ''
st2 = ''

for i in range(0, len(a)):
    if a[i] == '_':
        check = False
    if check == True:
        st1 += a[i]
    if (check == False) and (a[i] != '_'):
        st2 += a[i]
print(Greek[st1], Romann[st2])
