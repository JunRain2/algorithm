from collections import Counter


def solution(k, tangerine):
    counter = sorted(Counter(tangerine).values(), reverse=True)

    answer = 0
    for c in counter:
        k -= c
        answer += 1
        if k <= 0:
            break

    return answer
