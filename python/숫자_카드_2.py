from bisect import bisect_left, bisect_right

n = int(input())
n_array = list(map(int, input().split()))
n_array.sort()

m =  int(input())
m_array = list(map(int, input().split()))

result = []

for i in m_array:
    result.append(bisect_right(n_array, i) - bisect_left(n_array, i))
    
print(*result)