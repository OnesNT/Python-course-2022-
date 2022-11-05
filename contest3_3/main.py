a = str(input())
n = int(input())
d = {a[i: i + n] : a.count(a[i : i + n]) for i in range(len(a) - n + 1) if a.count(a[i: i + n]) >= 2}
print(sorted([key for key, val in d.items()]))
