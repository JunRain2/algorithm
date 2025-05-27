from itertools import combinations
from collections import deque

# 입력
n = int(input())
people = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in data[1:]:
        graph[i].append(j - 1)  # 인덱스는 0부터 시작

# 연결된지 확인하는 함수
def is_connected(area):
    visited = [False] * n
    q = deque()
    q.append(area[0])
    visited[area[0]] = True
    count = 1

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if next in area and not visited[next]:
                visited[next] = True
                q.append(next)
                count += 1
    return count == len(area)

# 가능한 모든 경우를 탐색
min_diff = float('inf')
for i in range(1, n // 2 + 1):
    for comb in combinations(range(n), i):
        area1 = list(comb)
        area2 = [x for x in range(n) if x not in area1]

        if is_connected(area1) and is_connected(area2):
            sum1 = sum(people[i] for i in area1)
            sum2 = sum(people[i] for i in area2)
            min_diff = min(min_diff, abs(sum1 - sum2))

# 출력
print(min_diff if min_diff != float('inf') else -1)