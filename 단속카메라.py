# 진입, 진출
def solution(routes):
    routes.sort()
    answer = 1

    start, end = routes[0]
    
    for i in range(1, len(routes)):
        if start <= routes[i][0] <= end:
            start = max(routes[i][0], start)
            end = min(routes[i][1], end)
        else:
            answer += 1
            start = routes[i][0]
            end = routes[i][1]
    
    return answer