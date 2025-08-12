def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent,a)
    b = find(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

n, m = map(int, input().split())

university = [''] + list(input().split())
edges = []

parent = list(range(n + 1))

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    
edges.sort()

result = 0
for c, a, b in edges:
    if find(parent, a) != find(parent, b) and university[a] != university[b]:
        result += c
        union(parent, a, b)

for i in range(1, n + 1):
    find(parent, i)
    
cnt = len(set(parent))
if cnt > 2:
    print(-1)
else:
    print(result)