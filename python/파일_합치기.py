import heapq

"""
각 장이 쓰여진 파일을 합쳐서 소설의 완성본이 들어있는 한 개의 파일

두 개의 파일이 합쳐서 하나의 임시 파일
임시파일이나 원래 파일을 계속 두 개씩 합쳐서 소설이 여러 장이 연속되도록 파일을 합쳐나가
최종적으로 하나의 파일

최종적인 한 개의 파일을 완성하는 데 필요한 비용의 총 합을 계산
최소 비용
"""
INF = int(1e9)

def solution(n, data):
    # 행 start, 열 end
    dp = [[INF] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    
    # 범위
    for step in range(1, n):
        for start in range(n - step):
            end = start + step
            mid = start
            while mid < end:
                dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid + 1][end])
                mid += 1
        
            dp[start][end] += sum(data[start:end + 1])
        
    return dp[0][n - 1]


for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    print(solution(n, data))