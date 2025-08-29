def solution(elements):
    n = len(elements)
    arr = elements * 2

    prefix = [0]
    for x in arr:
        prefix.append(prefix[-1] + x)  # 누적합

    answer = set()
    for size in range(1, n + 1):
        for start in range(n):
            answer.add(prefix[start + size] - prefix[start])
    return len(answer)
