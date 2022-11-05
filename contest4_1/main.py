# def fact(n):
#     temp = 1
#     for i in range (1, n + 1):
#         temp *= i
#     return temp
#
#
# def combination(n,  k):
#     return int(fact(n)) // int(fact(k) * fact(n - k)) ;
#
# def pascal_triangle() :
#     n1 = 0
#     while True:
#     # for n1 in range(x):
#         k1 = 0
#         while k1 <= n1:
#             print(combination(n1, k1), end = ' ')
#             k1 += 1
#         n1 += 1
#
# pascal_triangle()

def pascal_triangle():
    A = [1]
    while True:
        for i in A:
            yield i;
        B = [1]
        for i in range(1, len(A)):
            B.append(A[i - 1] + A[i])
        B.append(1)
        # print(B)
        A = B.copy()
# gen = pascal_triangle()
#
# for value in gen:
#     if value > 1000:
#         break
#     print(value, end = ' ')

