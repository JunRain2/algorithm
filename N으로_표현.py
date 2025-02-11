def solution(N, number):
    if N == number:
        return 1

    # dp[i]는 N을 (i+1)번 사용해서 만들 수 있는 모든 숫자들의 집합
    dp = [set() for _ in range(8)]
    
    for i in range(8):
        # N을 i+1번 이어 붙인 숫자 추가 (예: N=5일 때 5, 55, 555, ...)
        dp[i].add(int(str(N) * (i + 1)))
    
    for i in range(1, 8):
        for j in range(i):
            # dp[j]와 dp[i-j-1]에 있는 모든 숫자를 결합해 사칙 연산 수행
            for op1 in dp[j]:
                for op2 in dp[i - j - 1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        # 연산 후 해당 dp[i]에 목표 number가 있으면 (i+1)번 사용한 것이므로 반환
        if number in dp[i]:
            return i + 1

    return -1
