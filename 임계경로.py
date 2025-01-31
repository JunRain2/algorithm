from collections import deque

n = int(input())  # 도시의 개수
m = int(input())  # 도로의 개수

graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    reverse_graph[b].append((a, t))
    indegree[b] += 1

start, end = map(int, input().split())

# 1. 위상 정렬을 통한 최대 거리 계산
dist = [0] * (n + 1)
q = deque([start])

while q:
    now = q.popleft()
    for nxt, t in graph[now]:
        if dist[nxt] < dist[now] + t:
            dist[nxt] = dist[now] + t
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

# 2. 역방향 그래프를 이용하여 최대 경로에 사용된 간선 수 찾기
count_edge = 0
visited = [False] * (n + 1)
q = deque([end])

while q:
    now = q.popleft()
    for prev, t in reverse_graph[now]:
        if dist[now] - dist[prev] == t:
            count_edge += 1
            if not visited[prev]:
                visited[prev] = True
                q.append(prev)

# 결과 출력
print(dist[end])
print(count_edge)
