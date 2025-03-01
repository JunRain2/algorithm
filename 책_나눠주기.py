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

for tc in range(int(input())):
    n, m = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(m)]
    parent = list(range(n + 1))
    
    answer = 0
    for a, b in data:
        data = find_parent(parent, b)
        if data >= a:
            answer += 1
            union_parent(parent, data, data -1)
            for i in range(1, n + 1):
                find_parent(parent, i)
            
    print(answer)