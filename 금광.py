t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    array = [[] * m for _ in range(n)]
    
    for i in range(len(data)):
        array[i // m][i % m] = data[i]
    
    d = [[0] * m for _ in range(n)] # 더해갈 값
    for i in range(n):
        d[i][0] = array[i][0]
    
    dy = [-1, 0, 1]
    for i in range(n):
        for j in range(m - 1):
            y, x = i, j
            for k in range(3):
                nx = x + 1
                ny = y + dy[k]
                if ny >= 0 and y < n:
                    d[ny][nx] = max(d[y][x] + array[ny][nx], array[ny][nx])
    
    result = []            
    for i in range(n):
        result.append(d[i][len(m) - 1])
        
    print(max(result))
            