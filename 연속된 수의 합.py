from collections import deque

def solution(num, total):
    answer = deque()
    
    start = total
    end = total - num
    for i in range(start, end, -1):
        answer.append(i)
        
        
    while sum(answer) != total:
        answer.popleft()
        answer.append(end)
        end -= 1
        
    return sorted(answer)