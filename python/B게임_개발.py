from collections import deque

n = int(input())

graph = [[] for _ in range(n)]
indegree = [0] * n
build_time = [0] * n
result = [0] * n

for i in range(n):
    data = list(map(int, input().split()))
    # data[0]은 해당 건물의 건설 시간, 이어지는 수는 선행 건물 번호이며 -1로 끝난다
    build_time[i] = data[0]
    for x in data[1:]:
        if x == -1:
            break
        # x-1 건물이 먼저 지어져야 i번째 건물을 지을 수 있음
        graph[x - 1].append(i)
        indegree[i] += 1

q = deque()
# 진입차수가 0인 건물을 큐에 넣는다
for i in range(n):
    if indegree[i] == 0:
        q.append(i)
        result[i] = build_time[i]

while q:
    now = q.popleft()
    for nxt in graph[now]:
        # 선행 건물이 모두 지어지려면, 가장 오래 걸리는 경우로 갱신
        result[nxt] = max(result[nxt], result[now] + build_time[nxt])
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

for i in range(n):
    print(result[i])
