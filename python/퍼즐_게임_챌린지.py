def play_game(diffs, times, level):
    total_time = 0
    time_prev = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            total_time += times[i]
        else:
            diff = diffs[i] - level
            total_time += diff * (time_prev + times[i]) + times[i]
        time_prev = times[i]

    return total_time


# 퍼즐의 난이도, 현재 퍼즐의 소요 시간, 전체 제한 시간
def solution(diffs, times, limit):
    answer = 0

    start = 1
    end = max(diffs)
    while start <= end:
        mid = (start + end) // 2
        time = play_game(diffs, times, mid)

        if time <= limit:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    return answer
