from collections import deque
from copy import deepcopy

# 세로, 가로
n, m = map(int, input().split())
# 0은 빈 칸, 6은 벽, 1~5는 CCTV
graph = [list(map(int, input().split())) for _ in range(n)]
        
# 동, 남, 서, 북
dx = [0, 1, 0, -1] 
dy = [-1, 0, 1, 0]

# (x, y)
cctvs = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 5:
            # 4군대에 광선 발사 후 소비
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                while 0 <= nx < n and 0 <= ny < m:
                    # 6은 벽이기 때문에 break
                    if graph[nx][ny] == 6:
                        break
                    # 1 ~ 5는 통과 가능
                    elif graph[nx][ny] <= 0:
                        graph[nx][ny] -= 1
                    
                    nx, ny = nx + dx[i], ny + dy[i]
                    
        elif 1 <= graph[x][y] < 5:
            cctvs.append((x,y))
            
            
# cctv 유형별 방향 -> 4가지 방향을 + 1 해가면서 돌릴 예정
direct = [[0], [0, 2], [0, 3], [0, 2, 3]]

# 현재 좌표, 몇 번째 방향인지, 그래프
def monitor(x, y, dir, graph):
    current_dir = [(i + dir) % 4 for i in direct[graph[x][y] - 1]]
    
    # 방향, 해당 방향으로 쭉 광선을 발사
    for d in current_dir:
        nx, ny = x + dx[d], y + dy[d]       
        while 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 6:
                break
            elif graph[nx][ny] <= 0:
                graph[nx][ny] -= 1
            nx, ny = nx + dx[d], ny + dy[d]
    
    return graph

q = deque(cctvs)

# 그래프 CCTV 사각지대 범위 계산
def cnt_cctv_range(graph):
    result = 0
    for x in range(n):
        for y in range(m):
            result += graph[x][y] == 0
                
    return result


def dfs(q, graph):
    # 탐색이 모두 끝났을 때 
    if not q:
        return cnt_cctv_range(graph)
    
    x, y = q.popleft()
    result = 1e9
    for i in range(4):
        copy_graph = deepcopy(graph)
        # 현재 x, y의 cctv범위를 계산해서 다음으로 넘김, 이후 최솟값을 반환
        result = min(dfs(q, monitor(x, y, i ,copy_graph)), result)
    q.append((x, y))
    
    return result

print(dfs(q, graph))