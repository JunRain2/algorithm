def solution(n, w, num):
    answer = 0

    if w == 1:
        return n - num + 1

    num -= 1
    n -= 1

    x, y = divmod(num, w)
    if x % 2 == 1:
        y = w - y - 1

    ex, ey = divmod(n, w)

    answer += ex - x

    if ex % 2 == 1:
        ey = w - ey - 1
        answer += ey <= y < w
    else:
        answer += 0 <= y <= ey

    return answer
