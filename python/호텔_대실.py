import heapq

def solution(book_time):
    answer = 0
    bt = []

    for a, b in book_time:
        start = list(map(int, a.split(":")))
        end = list(map(int, b.split(":")))
        
        bt.append((start[0] * 60 + start[1], end[0] * 60 + end[1] + 10))
        
    bt.sort()
    print(bt)
    
    q = []
    for b in bt:
        heapq.heappush(q, b[1])
        
        while q:
            m = heapq.heappop(q)
            # 현재 방의 시작점이, 큐의 끝나는 시간보다 작은 경우
            if b[0] >= m:
                continue
            else:
                heapq.heappush(q, m)
                break
        
        answer = max(answer, len(q))
        
    return answer