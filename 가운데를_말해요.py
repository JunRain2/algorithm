from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    mid = i // 2
    a = int(input())
    if not array or array[-1] <= a:
        array.append(a)
    else:
        array.insert(bisect_left(array, a), a)
    print(array[mid])