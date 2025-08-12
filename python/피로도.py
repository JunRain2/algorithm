def dfs(k, dungeons, visited, count):
    max_count = count
    for i in range(len(dungeons)):
        if not visited[i] and dungeons[i][0] <= k:
            visited[i] = True
            max_count = max(dfs(k - dungeons[i][1], dungeons, visited, count + 1), max_count)
            visited[i] = False 
    return max_count

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    return dfs(k, dungeons, visited, 0)
