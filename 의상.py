from collections import Counter
from itertools import combinations


def solution(clothes):
    answer = 0
    kind_counter = dict(Counter([x[1] for x in clothes]))
    clothes_cnt = kind_counter.values()

    for i in range(1, len(clothes_cnt)):
        for j in combinations(clothes_cnt, i):
            tmp = 1
            for k in j:
                tmp *= k
        answer += tmp

    return answer
