import heapq

def solution(n, times):
    answer = 0
    waits = []
    for time in times:
        heapq.heappush(waits, (time, time))
    
    for _ in range(n - 1):
        wait, time = heapq.heappop(waits)
        heapq.heappush(waits, (wait + time, time))
    
    answer, tmp = heapq.heappop(waits)
    return answer