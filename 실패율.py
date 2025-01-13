def solution(N, stages):
    answer = []
    tmp = []
    
    result = [0] * (N + 2)
    for i in stages:
        result[i] += 1
        
    cnt = len(stages)
    for i in range(1, N + 1):
        if cnt <= 0:
            tmp.append((i, 0))
            continue
        tmp.append((i, result[i]/cnt))
        cnt -= result[i]
    
    tmp.sort(key = lambda x: (-x[1], x[0]))
    
    for i in tmp:
        answer.append(i[0])
    
    return answer