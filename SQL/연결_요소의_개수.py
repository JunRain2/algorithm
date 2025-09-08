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

n, m = map(int, input().split())
parent = list(range(n + 1))

for _ in range(m):
    a, b = map(int, input().split())
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        
for i in range(1, n + 1):
    find(parent, i)

result = set(parent)
result.remove(0)
print(len(result))