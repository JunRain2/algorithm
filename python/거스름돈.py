def solution(n, money):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1  # 0원을 만드는 방법은 1가지

    # 동전을 바깥 반복문으로 처리하여 각 동전이 한번씩만 고려되도록 함
    for coin in money:
        # coin 이상의 금액부터 n까지, coin을 추가하여 만드는 경우의 수를 누적
        for i in range(coin, n + 1):
            dp[i] = (dp[i] + dp[i - coin]) % MOD

    return dp[n]
