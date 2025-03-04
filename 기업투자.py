n, m = map(int, input().split())
profits = [[0] * (n + 1)] + [list(map(int, input().split())) for _ in range(n)]

# DP 테이블과 역추적 배열 (행: 기업, 열: 투자금액)
dp = [[0] * (n + 1) for _ in range(m + 1)]
invest = [[0] * (n + 1) for _ in range(m + 1)]

# DP 계산
for company in range(1, m + 1):  # 기업 번호
    for money in range(n + 1):  # 총 투자 금액
        dp[company][money], invest[company][money] = max(
            (dp[company - 1][money - invest_amount] + profits[invest_amount][company], invest_amount)
            for invest_amount in range(money + 1)
        )

# 최대 이익 출력
print(dp[m][n])

# 역추적하여 각 기업의 투자 금액 구하기
result = [0] * m
remaining_money = n
for company in range(m, 0, -1):
    result[company - 1] = invest[company][remaining_money]
    remaining_money -= invest[company][remaining_money]

print(*result)
