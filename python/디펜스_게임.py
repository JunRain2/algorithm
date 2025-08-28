import heapq

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    max_heap = []  # 무적권을 사용할 가장 큰 적들을 저장
    soldiers = n
    
    for i, e in enumerate(enemy):
        # 현재 적을 힙에 추가 (최대힙을 위해 음수로 저장)
        heapq.heappush(max_heap, -e)
        soldiers -= e
        
        # 병사가 부족하면 무적권 사용
        if soldiers < 0:
            if k > 0:
                # 가장 큰 적에게 무적권 사용
                largest = -heapq.heappop(max_heap)
                soldiers += largest
                k -= 1
            else:
                # 무적권도 없으면 게임 오버
                return i
    
    return len(enemy)

"""
일단 병사를 줄이고, 병사가 부족해졌을 때 무적권을 회복권처럼 사용하여 풀이
"""