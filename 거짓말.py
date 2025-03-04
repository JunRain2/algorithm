# 과장된 이야기를 할 수 있는 파티 개수의 최댓값
# 사람의 수, 파티의 수
n, m = map(int, input().split())
# 진실을 아는 사람의 수와 번호
array = list(map(int, input().split()))

data = []
for i in range(m):
    data.append(list(map(int, input().split())))

parent = list(range(n + 1))


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


for i in data:
    for j in range(1, i[0]):
        if find(parent, i[j]) != find(parent, i[j + 1]):
            union(parent, i[j], i[j + 1])
            
for i in range(1, n + 1):
    find(parent, i)

t = set()
for i in range(1, array[0] + 1):
    t.add(parent[array[i]])

for i in data:
    for j in range(1, i[0] + 1):
        if find(parent, i[j]) in t:
            m -= 1
            break
        
print(m)