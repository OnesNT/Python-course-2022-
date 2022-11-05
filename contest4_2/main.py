# sq1 = list(input())
# sq2 = list(input())
# from heapq import merge
#
# sq1 = [1, 3, 4, 4]
# sq2 = [1, 3, 21, 1, 2 ]
# ls = merge(sq1 , sq2 )
# while True:
#     print(next(ls))
# def merge_sorter(*arg):
#
#     from heapq import merge
#     item = iter(merge(arg))
#     while True:
#         try:
#             # Try to get next element
#             yield next(item)
#         except StopIteration:
#             # Iteration is finished. You can type your code here:
#             pass
#
# gen = merge_sorter([10, 9 , 0 , 2 ,3])
#
# while True:
#     print(next(gen))
# while True:
#     print(next(gen1))
# print(list(gen1))
# gen = merge_sorter(gen1, sq1)
# while True:
#     print(next(gen))
#
# from heapq import merge
# st = [9,3,2,4,2]
# gen = merge(iter(st))
# while True:
#     print(next(gen))





a = merge_sorter(1,2,2,1,3,4,1)
while True:
    print(next(a))