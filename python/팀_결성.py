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


v, e = map(int, input().split())

parent = [0] * (v + 1)
for i in range(0, v + 1):
    parent[i] = i

result = list()

for _ in range(e):
    a, x, y = map(int, input().split())
    if a == 0:
        union_parent(parent, x, y)
    elif a == 1:
        result.append(find_parent(parent, x) == find_parent(parent, y))

for i in result:
    if i:
        print("YES")
    else:
        print("NO")
