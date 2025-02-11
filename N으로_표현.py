# 수를 붙이는 경우의 수, 사칙연산의 경우의 수
def solution(N, number):
    answer = 0
    dp = [8] * 1000000
    for i in range(1, N):
        dp[i] = i*2
    dp[N] = 1
    
    for i in range(1, 32001):
        # i + N
        if 0 < i + N < 32001:
            dp[i + N]  = min(dp[i] + 1, dp[i + N])
        # i * N
        if 0 < i * N < 32001:
            dp[i * N] = min(dp[i] + 1, dp[i * N])
        # i / N
        if 0 < i // N < 32001:
            dp[i//N] = min(dp[i] + 1, dp[i//M])
        # i - N
        if 0 < i - N < 32001:
            dp[i - N] = min(dp[i] + 1, dp[i - N])
        # ii
        if set(list(str(i))) == set([str(N)]):
            num = int(str(i) + str(N))
            if 0 < num < 32001:
                dp[num] = min(dp[num], dp[i] + 1)
    
    answer = -1 if dp[number] >= 8 else dp[number]
    return answer