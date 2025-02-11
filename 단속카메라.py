# 진입, 진출
def solution(routes):
    routes.sort()    
    answer = 1
    
    start = routes[0][0]
    end = routes[0][1]
    
    for i in range(1, len(routes)):
        if start <= routes[i][0] <= end:
            start = routes[i][0]
        else:
            answer += 1
            start = routes[i][0]
            end = routes[i][1]
    
    return answer