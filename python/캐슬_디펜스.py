from itertools import combinations
from collections import deque
import copy

n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 궁수 턴 종료 시, 적이 전진하는 메서드
def forward(g):
    for i in range(n-1, 0, -1):
        g[i] = g[i - 1]
    g[0] = [0] * m

# 모든 적이 필드에서 제외되었는지 확인하는 메서드    
def check_end(g):
    for i in range(n):
        if 1 in g[i]:
            return True #적이 존재하기 때문에 게임을 지속
    
    return False # 적이 존재하기 때문에 게임을 끝냄

# 궁수가 적을 잡는 메서드
# 궁수들이 적을 동시에 공격하는 로직
def attack(g, archers):
    n, m = len(g), len(g[0])
    targets = set()  # 중복 타깃 제거용

    for col in archers:
        visited = [[False]*m for _ in range(n)]
        q = deque()
        q.append((n-1, col, 1))  # 궁수는 항상 마지막 행에서 시작, 거리 1

        while q:
            x, y, dist = q.popleft()
            if dist > d:
                break

            if 0 <= x < n and 0 <= y < m and not visited[x][y]:
                visited[x][y] = True
                if g[x][y] == 1:
                    targets.add((x, y))
                    break  # 이 궁수는 타깃을 찾았으므로 종료

                # 왼쪽, 위, 오른쪽 순으로 탐색 (← ↑ →)
                for dx, dy in [(0, -1), (-1, 0), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        q.append((nx, ny, dist + 1))

    # 타깃 제거 및 제거 수 반환
    count = 0
    for x, y in targets:
        if g[x][y] == 1:
            g[x][y] = 0
            count += 1
    return count
            

result = 0
for c in combinations(list(range(m)), 3):
    cnt = 0
    g = copy.deepcopy(graph)
    
    while check_end(g):
        cnt += attack(g, c)
        forward(g)
    
    result = max(result, cnt)

print(result)