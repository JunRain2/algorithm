N = int(input())

max_H = 0
max_L = 0
max_H_index = 0
numbers = []
for _ in range(N):
    L, H = map(int, input().split())
    numbers.append([L, H])

    if H > max_H:
        max_H = H
        max_H_index = L

    if L > max_L:
        max_L = L

targetList = [0] * (max_L + 1)
for l, h in numbers:
    targetList[l] = h

w = 0

# 왼쪽에서 더하기
temp = 0
for i in range(max_H_index + 1):
    if targetList[i] > temp:
        temp = targetList[i]

    w += temp

# 오른쪽에서 더하기
temp = 0
for i in range(max_L, max_H_index, -1):
    if targetList[i] > temp:
        temp = targetList[i]

    w += temp

print(w)