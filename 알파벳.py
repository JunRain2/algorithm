def dfs(x, y, alphabets):
    if x < 0 or x >= r or y < 0 or y >= c or array[x][y] in alphabets:
        return 0
    
    alphabets.add(array[x][y])
    max_length = 0
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        max_length = max(max_length, dfs(nx, ny, alphabets))
    
    alphabets.remove(array[x][y])
    return max_length + 1

r, c = map(int, input().split())
array = [input() for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(dfs(0, 0, set()))
