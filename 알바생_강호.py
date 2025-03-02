n = int(input())
array = [int(input()) for _ in range(n)]
array.sort(reverse=True)

result = 0
for i in range(n):
    result += max(0, array[i] - i)

print(result)
