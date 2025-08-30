def solution(topping):
    answer = 0
    n = len(topping)
    
    tmp_set = set()
    forward = []
    for t in topping:
        tmp_set.add(t)
        forward.append(len(tmp_set))
        
    tmp_set = set()
    for i in range(n-1, 0, -1):
        tmp_set.add(topping[i])
        if forward[i - 1] == len(tmp_set):
            answer += 1
    
    return answer