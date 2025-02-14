# [i][0] A도둑, [i][1] B도둑, A 최소 흔적, B 최소 흔적
def solution(info, n, m):
    answer = 0
    # B 도둑을 기준으로 그리드로 풀이
    info.sort(key=lambda x: (x[1], x[0]))

    a = n
    b = m
    for i, inf in enumerate(info):
        if inf[1] < b:
            b -= inf[1]
        elif inf[0] < a:
            a -= inf[0]
            answer += inf[0]
        else:
            return -1

    return answer
