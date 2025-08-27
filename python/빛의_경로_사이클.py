dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(grid):
    answer = []
    grid = [list(row) for row in grid]
    x_dist = len(grid)
    y_dist = len(grid[0])

    visited = [[[False] * 4 for _ in range(y_dist)] for _ in range(x_dist)]

    def find_cycle(start_x, start_y, start_dir):
        x, y, direction = start_x, start_y, start_dir
        path = []

        while not visited[x][y][direction]:
            visited[x][y][direction] = True
            path.append((x, y, direction))

            # 방향 변경
            if grid[x][y] == "L":
                direction = (direction - 1) % 4
            elif grid[x][y] == "R":
                direction = (direction + 1) % 4

            # 다음 위치
            x = (x + dx[direction]) % x_dist
            y = (y + dy[direction]) % y_dist

        return len(path)

    for i in range(x_dist):
        for j in range(y_dist):
            for d in range(4):
                if not visited[i][j][d]:
                    cycle_length = find_cycle(i, j, d)
                    if cycle_length > 0:
                        answer.append(cycle_length)

    return sorted(answer)
