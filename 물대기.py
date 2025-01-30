n = int(input())
array = [int(input()) for _ in range(n)]
edges = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] != 0:
            edges.append((data[j], i, j))

edges = list(edges)
edges.sort()

parent = [i for i in range(n)]


# 모든 거리 + 제일 작은 비용
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


result = 0
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

group = [[] for _ in range(n)]
for i in range(n):
    group[parent[i]].append(array[i])

for i in range(n):
    if group[i]:
        result += min(group[i])

print(result)
