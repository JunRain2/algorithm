def solution(sequence, k):
    start = end = s = 0
    best = [0, len(sequence)]  # 최악의 경우로 초기화

    while end < len(sequence):
        s += sequence[end]

        while s > k:
            s -= sequence[start]
            start += 1

        if s == k and end - start < best[1] - best[0]:
            best = [start, end]

        end += 1

    return best
