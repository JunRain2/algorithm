def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 집의 수 m, 길의 수 n
while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    parent = list(range(m))

    sum = 0
    edges = []
    for i in range(n):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
        sum += c

    edges.sort()

    result = 0
    for c, a, b in edges:
        if find(parent, a) != find(parent, b):
            result += c
            union(parent, a, b)
            
    print(sum - result)
