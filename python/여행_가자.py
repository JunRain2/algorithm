def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(input())  # 도시의 수
m = int(input())  # 여행 계획에 속한 도시들의 수

parent = list(range(n + 1))

for i in range(1, n + 1):
    a = [0] + list(map(int, input().split()))
    for j in range(1, n + 1):
        if a[j] == 1 and find(parent, i) != find(parent, j):
            union(parent, i, j)
            
for i in range(1, n + 1):
    find(parent, i)
    
plan = list(map(int, input().split()))
check = parent[plan[0]]
for i in range(1, m):
    if check != parent[plan[i]]:
        print("NO")
        exit()
print("YES")