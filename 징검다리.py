# 출발지점부터 도착지까지의 거리, 바위 위치, 제거할 바위의 수
def solution(distance, rocks, n):
    answer = 0
    
    rocks.append(distance)
    rocks.sort()
    start, end = 1, distance
    
    while start <= end:
        mid = (start + end) // 2
        current = removed = 0
        
        for rock in rocks:
            if rock - current < mid:
                removed += 1
            else:
                current = rock
        
        if removed > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    
    return answer