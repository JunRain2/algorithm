n = int(input())
m = int(input())
arr = list(map(int, input().split()))

s = set(arr)

result = 0
for i in arr:
    if m - i in s:
        result += 1
            
print(result//2)