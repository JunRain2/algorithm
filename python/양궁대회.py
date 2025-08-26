def solution(n, info):
    best = None
    max_diff = 0

    def score_diff(lion_alloc):
        a, l = 0, 0
        for i in range(11):
            s = 10 - i
            if info[i] == 0 and lion_alloc[i] == 0:  # 이 부분이 핵심!
                continue
            if lion_alloc[i] > info[i]:
                l += s
            else:
                a += s
        return l - a

    def dfs(i, left, ryan):
        nonlocal best, max_diff

        if i == 11:
            if left:
                ryan[10] += left  # 0점에 몰아주기

            diff = score_diff(ryan)

            if diff > 0 and (
                diff > max_diff or (diff == max_diff and ryan[::-1] > best[::-1])
            ):
                best, max_diff = ryan[:], diff

            if left:
                ryan[10] -= left  # 백트래킹
            return

        dfs(i + 1, left, ryan)
        if left >= info[i] + 1:
            ryan[i] = info[i] + 1
            dfs(i + 1, left - info[i] - 1, ryan)
            ryan[i] = 0

    dfs(0, n, [0] * 11)
    return best if best else [-1]
