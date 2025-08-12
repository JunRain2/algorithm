from bisect import bisect_left, bisect_right

t = int(input())
n = int(input())
a_array = list(map(int, input().split()))
m = int(input())
b_array = list(map(int, input().split()))
a_sum = []
b_sum = []

# 모든 a[i] ~ a[j]의 경우의 수
for i in range(n):
    s = a_array[i]
    a_sum.append(s)
    for j in range(i + 1, n):
        s += a_array[j]
        a_sum.append(s)

for i in range(m):
    s = b_array[i]
    b_sum.append(s)
    for j in range(i + 1, m):
        s += b_array[j]
        b_sum.append(s)

a_sum.sort()
b_sum.sort()
result = 0
for i in range(len(a_sum)):
    left = bisect_left(b_sum, t - a_sum[i])
    right = bisect_right(b_sum, t - a_sum[i])
    result += right - left

print(result)
