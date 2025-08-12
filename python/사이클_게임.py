# 홀수, 짝수, 돌아가면서 진행
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
parent = list(range(n))

array = [tuple(map(int, input().split())) for _ in range(m)]

answer = 0
for i in range(m):
    a, b = array[i]
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
    else:
        answer = i + 1
        break

print(answer)