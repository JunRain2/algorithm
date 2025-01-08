def solution(n, weak, dist):
    answer = 0

    weak_dist = []  # cost, x, y 순/ weak의 거리
    for i in range(len(weak)):
        x, y = weak[i], weak[(i + 1) % len(weak)]
        cost = y - x
        if cost < 0:
            cost = (y + n) - x
        weak_dist.append((cost, x, y))

    weak_dist.sort(reverse=True)

    return answer
