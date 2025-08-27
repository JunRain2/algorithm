def solution(grid):
    # 북동남서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    rows, cols = len(grid), len(grid[0])
    global_visited = set()  # 전체적으로 이미 처리된 상태들
    cycles = []
    
    def simulate_light(start_x, start_y, start_dir):
        x, y, direction = start_x, start_y, start_dir
        local_visited = set()  # 현재 경로에서 방문한 상태들
        
        while (x, y, direction) not in local_visited:
            if (x, y, direction) in global_visited:
                # 이미 다른 사이클에서 처리된 경로
                return 0
                
            local_visited.add((x, y, direction))
            
            # 현재 위치의 명령에 따라 방향 변경
            if grid[x][y] == 'L':
                direction = (direction - 1) % 4
            elif grid[x][y] == 'R':
                direction = (direction + 1) % 4
            
            # 다음 위치 계산
            x = (x + dx[direction]) % rows
            y = (y + dy[direction]) % cols
        
        # 사이클 발견 - 모든 방문한 상태를 global에 추가
        global_visited.update(local_visited)
        return len(local_visited)
    
    # 모든 가능한 시작점에서 시뮬레이션
    for i in range(rows):
        for j in range(cols):
            for direction in range(4):
                if (i, j, direction) not in global_visited:
                    cycle_length = simulate_light(i, j, direction)
                    if cycle_length > 0:
                        cycles.append(cycle_length)
    
    return sorted(cycles)