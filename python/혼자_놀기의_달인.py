def solution(cards):
    visited = [False] * len(cards)
    groups = []
    
    for i in range(len(cards)):
        if visited[i]:
            continue
            
        # 사이클 길이 계산
        current = i
        length = 0
        while not visited[current]:
            visited[current] = True
            current = cards[current] - 1  # 1-based → 0-based
            length += 1
        
        groups.append(length)
    
    groups.sort(reverse=True)
    return groups[0] * groups[1] if len(groups) >= 2 else 0