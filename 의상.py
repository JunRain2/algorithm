from collections import Counter
from itertools import combinations

def solution(clothes):
    kind_counter = dict(Counter([x[1] for x in clothes]))
    clothes_cnt = kind_counter.values()
    
    answer = 1
    for cnt in clothes_cnt:
        answer *= (cnt + 1)

    return answer - 1