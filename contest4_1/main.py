def pascal_triangle():
    A = [1]
    while True:
        for i in A:
            yield i;
        B = [1]
        for i in range(1, len(A)):
            B.append(A[i - 1] + A[i])
        B.append(1)
        A = B.copy()


