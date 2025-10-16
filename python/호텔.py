# 최소 c명, n개의 도시
INF = int(1e9)

c, n = map(int, input().split())

# index 명일 때 최소 cost
dp = [INF for _ in range(c + 101)]

# 홍보 비용, 얻을 수 있는 인수
arr = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(1, c + 101):
    for cost, person in arr:
        if i - person > 0:
            dp[i] = min(dp[i], dp[i - person] + cost) 
        else:
            dp[i] = min(dp[i], cost)

print(min(dp[c:-1]))