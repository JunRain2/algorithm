from collections import deque

n = int(input())

# 위상 정렬 -> edges가 주어줘야 함.
graph = [[] for _ in range(n + 1)]
times = [0] * (n + 1)
indegrees = [0] * (n + 1)

for i in range(1, n + 1):
    # 작업이 걸리는 시간, 해당 작업을 진행하기 위해 선행해야할 작업의 수, 작업들 ~~~
    data = list(map(int, input().split()))
    times[i] = data[0]
    
    for j in range(2, len(data)):
        graph[data[j]].append(i)
        indegrees[i] += 1

q = deque()
result = [0] * (n + 1)

for i in range(n + 1):
    if indegrees[i] == 0:
        q.append(i)
        result[i] = times[i]

while q:
    n = q.popleft()
    
    for i in graph[n]:
        indegrees[i] -= 1
        result[i] = max(result[i], result[n] + times[i])
        if indegrees[i] == 0:
            q.append(i)
            
print(max(result))