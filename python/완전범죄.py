# [i][0] A도둑, [i][1] B도둑, A 최소 흔적, B 최소 흔적

INF = int(1e9)


def solution(info, n, m):
    answer = 0

    dp = {}  # (i, a, b)를 키로 하는 메모제이션(dict())

    def back_traking(a, b, i):
        if a >= n or b >= m:
            return INF
        if i == len(info):
            return a
        if (i, a, b) in dp:
            return dp[(i, a, b)]

        mv = min(
            back_traking(a + info[i][0], b, i + 1),
            back_traking(a, b + info[i][1], i + 1),
        )
        dp[(i, a, b)] = mv
        return mv

    answer = back_traking(0, 0, 0)
    if answer >= INF:
        return -1

    return answer