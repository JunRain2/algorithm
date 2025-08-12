from collections import deque

n = int(input())  # n번째는 완제품
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
m = int(input())

for _ in range(m):
    # x를 만드는데 y가 k개 필요
    x, y, k = map(int, input().split())
    graph[x].append((y, k))
    indegree[y] += 1


q = deque()
result = [0] * (n + 1)

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

# 기본 제품을 걸러내는 과정
tmp = []
for i in range(1, n + 1):
    if not graph[i]:
        tmp.append(i)

while q:
    v = q.popleft()
    for y, k in graph[v]:
        indegree[y] -= 1
        if result[v] == 0:
            result[y] += k
        else:
            result[y] += result[v] * k
        if indegree[y] == 0:
            q.append(y)

tmp.sort()
for i in tmp:
    print(i, result[i])
