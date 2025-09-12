def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = parent[a]
    b = parent[b]
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(int(input())):
    # 국가의 수, 비행기 종류
    n, m = map(int, input().split())
    parent = list(range(n + 1))
    
    result = 0
    for _ in range(m):
        a, b = map(int, input().split())
        
        if find(parent, a) != find(parent, b):
            result += 1
            union(parent, a, b)
    
    print(result)
        
    # 몇 번 탔느냐가 아닌 비행기의 종류를 리턴해야 함
    