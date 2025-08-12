from collections import Counter

for tc in range(int(input())):
    n = int(input())
    a = list(input())  # 초기
    a_counter = Counter(a)
    b = list(input())  # 목표
    b_counter = Counter(b)

    diff = abs(a_counter["W"] - b_counter["W"])

    cnt = sum(c1 != c2 for c1, c2 in zip(a, b))

    print((cnt - diff) // 2 + diff)
