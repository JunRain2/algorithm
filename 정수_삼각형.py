n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
    
dp = [[0] * len(array[n-1]) for _ in range(n)]
dp[0][0] = array[0][0]
    
for i in range(1, n):
    for j in range(len(array[i])):
        if j == 0:
            left = 0
        else:
            left = dp[i - 1][j - 1]
            
        right = dp[i - 1][j]
        dp[i][j] = max(left, right) + array[i][j]
        
print(max(dp[n - 1]))