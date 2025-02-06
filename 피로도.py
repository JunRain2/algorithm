def dfs(k, v, visitd, dungeons, cnt):
    if k < 0 or cnt == len(dungeons):
        return cnt
    max_cnt = cnt
    for i in range(len(dungeons)):
        if not visitd[i] or dungeons[i][0] <= k:
            visitd[i] = True
            max_cnt = max(dfs(k - dungeons[i][1], i, visitd, dungeons, cnt + 1), max_cnt)
            visitd[i] = False 
    return max_cnt

def solution(k, dungeons):
    answer = -1
    visitd = [False] * len(dungeons)
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            visitd[i] = True
            answer = max(dfs(k, i, visitd, dungeons, 0), answer)
            visitd[i] = False
        
    return answer