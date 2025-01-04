from collections import deque


n = int(input())

graph = [[] for _ in range(n + 1)]
times = [0] * (n + 1)
result = [0] * (n + 1)
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    input_list = list(map(int, input().split()))
    times[i] = input_list.pop(0)

    for j in input_list:
        if j == -1:
            break
        graph[j].append(i)
        indegree[i] += 1


def topology_sort():
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = times[i]

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], times[i] + result[now])
            
            if indegree[i] == 0:
                q.append(i)


topology_sort()

for i in range(1, n + 1):
    print(result[i])
