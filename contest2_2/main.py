
Roman_num = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI',
            'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX',
            'XXX')

Greek_alpha = ('alpha_', 'beta_', 'gamma_', 'delta_', 'epsilon_', 'zeta_', 'eta_', 'theta_', 'iota_', 'kappa_')

a = int(input())
b = int(input())
if a == 0 or b == 0:
    dosmt = None
else:
    for i in range(0, a):
        for j in range(0, b - 1):
            print(Greek_alpha[i] + Roman_num[j], end = ' ')
        print(Greek_alpha[i] + Roman_num[b - 1], end = '')
        print()
