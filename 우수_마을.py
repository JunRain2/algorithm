import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().strip())
# 주민 수를 인덱스 1부터 사용하기 위해 0을 앞에 추가합니다.
population = [0] + list(map(int, input().split()))

# 무방향 트리 구성을 위한 인접 리스트 생성
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# dp[node][0] : node가 우수 마을이 아닌 경우의 최대 주민 수 합
# dp[node][1] : node가 우수 마을인 경우의 최대 주민 수 합
dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(node):
    visited[node] = True
    # 현재 마을을 우수 마을로 선정한 경우 주민 수는 해당 마을의 인구 수부터 시작
    dp[node][1] = population[node]
    dp[node][0] = 0
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)
            # 부모 마을이 우수 마을이 아닐 경우, 자식 마을은 우수 마을일 수도, 아닐 수도 있으므로 둘 중 큰 값을 선택
            dp[node][0] += max(dp[neighbor][0], dp[neighbor][1])
            # 부모 마을이 우수 마을로 선정되면 인접 마을은 선택할 수 없으므로, 자식 마을은 무조건 우수 마을이 아닌 경우의 값만 추가
            dp[node][1] += dp[neighbor][0]

dfs(1)
# 루트 마을(1번)을 기준으로 우수 마을 선정 여부에 따른 최대 주민 수 합을 출력합니다.
print(max(dp[1][0], dp[1][1]))
