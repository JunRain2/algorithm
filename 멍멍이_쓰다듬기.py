def solve():
    dif = b - a
    day = 0
    for i in range(1, 2 ** 31):
        for _ in range(2):
            if dif <= 0:
                return day
            day += 1
            dif -= i


a, b = map(int, input().split())
print(solve())