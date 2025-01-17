# 탑승구 문제의 개념으로 풀이
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

array = []
max_day = 0
for _ in range(n):
    p, d = map(int, input().split())
    array.append((p, d))
    max_day = max(max_day, d)

parent = [i for i in range(max_day + 1)]
array.sort(key=lambda x: (-x[0], -x[1]))
cost = 0

for p, d in array:
    data = find_parent(parent, d)
    if data != 0:
        cost += p
        union_parent(parent, data, data - 1)

print(cost)
