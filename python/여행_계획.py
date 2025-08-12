n, m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
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
        
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i
        
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i + 1, j + 1)
            
array = list(map(int, input().split()))

flag = True
for i in range(len(array) - 1):
    if find_parent(parent, array[i]) != find_parent(parent, array[i + 1]):
        flag = False
        break
    
if flag:
    print("YES")
else:
    print("NO")