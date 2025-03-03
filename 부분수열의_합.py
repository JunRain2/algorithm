n = int(input())
s = list(map(int, input().split()))
s.sort()

target = 1
for i in s:
    if i > target:
        break
    target += i

print(target)
