# 중점(0), 위(1), 왼쪽(2), 아래(3), 오른쪽(4)
# 시작은 중점, 한 번에 한 발만 움직여야 함
# 게임 시작을 제외하고 두 발이 같이 있어서는 안됨


arr = list(map(int, input().split()))
n = len(arr)

arr = arr[:len(arr) - 1]

# 힘의 크기가 다 다름
    # 같은 지점 -> 1
    # 중앙에서 이동 -> 2
    # 인접(왼 -> 위 / 왼 -> 오) -> 3
    # 반대(왼 -> 오 / 위 -> 아) -> 4
def add_power(s, e):
    if s == e:
        return 1
    elif s == 0:
        return 2
    elif (s + 1) % 5 == e or (s - 1) % 5 == e:
        return 3
    
    return 4

# 현재 위치 = min(현재 위치, 왼발 움직였을 때, 오른발 움직였을 때)
INF = int(1e9)
dp = [[INF, (0, 0)] * 2 for _ in range(n)]

dp[0][0] = [0, (0, 0)]
dp[0][1] = [0, (0, 0)]

for i in range(1, n):
    # 이전에서 왼 발 움직였을 때
    for j in range(2):
        p, (x, y) = dp[i - 1][j]
        if y == arr[i]:
            continue
        p += add_power(x, arr[i])
        
        if dp[i][0][0] < p:
            dp[i][0] = 
        
    
    # 이전에서 오른 발 움직였을 때
    dp[i][1] = min(dp[i - 1][0], dp[i- 1][1])
    
print(min(dp[n- 1]))