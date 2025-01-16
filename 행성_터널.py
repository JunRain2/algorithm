import sys

input = sys.stdin.readline


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

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i


# N * N의 거리 계산하여 Edges에 넣는 과정 필요
planet = [(0, 0, 0)]
for _ in range(n):
    planet.append(tuple(map(int, input().split())))


edges = []
for i in range(1, n):
    for j in range(i + 1, n + 1):
        ax, ay, az = planet[i]
        bx, by, bz = planet[j]
        cost = min(abs(ax - bx), abs(ay - by), abs(az - bz))
        edges.append((cost, i, j))


edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(result)
