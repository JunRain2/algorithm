# 배포되어야 하는 순서대로 작업의 진도, 각 작업의 개발 속도
import math


def solution(progresses, speeds):
    answer = []
    top = math.ceil((100 - progresses[0]) / speeds[0])
    day = [top]
    for i in range(1, len(speeds)):
        value = math.ceil((100 - progresses[i]) / speeds[i])
        if top < value:
            top = value
            answer.append(len(day))
            day = []
        day.append(value)

    if len(day) != 0:
        answer.append(len(day))

    return answer
