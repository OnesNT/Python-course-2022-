n = int(input())
F = [3, 8]
for i in range(2, n):
    F.append(2*(F[i - 1] + F[i - 2]))
print(F[n - 1])