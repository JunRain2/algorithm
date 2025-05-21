from itertools import combinations
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
def attack(g, k):
    for j in range(m):
        for i in range(n-1, -1, -1):
            if g[i][j] == 1:
                distance = abs(n - i) + abs(k - j)
                if distance <= d:
                    g[i][j] = 0
                    return 1
    return 0
            

result = 0
for c in combinations(list(range(m)), 3):
    cnt = 0
    g = copy.deepcopy(graph)
    
    while check_end(g):
        for k in c:
            cnt += attack(g, k)
        forward(g)
    
    result = max(result, cnt)

print(result)