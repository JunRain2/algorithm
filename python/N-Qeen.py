def solution(n):
    answer = 0
    # [row] = col 이 퀸의 위치
    board = [0] * n

    def back_track(row):
        nonlocal answer

        # 마지막에 도달했을 경우
        if row == n:
            answer += 1
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                back_track(row + 1)

    def is_safe(row, col):
        for i in range(row):
            # 이전 행에 같은 col이 존재하거나 대각선에 퀸이 존재하는 경우
            # 행과 열의 차이
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False

        return True

    back_track(0)
    return answer
