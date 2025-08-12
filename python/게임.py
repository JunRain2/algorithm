x, y = map(int, input().split())  # 게임 횟수, 이긴 게임

z = (y * 100) // x

result = -1
start, end = 1, x

while start <= end:
    mid = (start + end) // 2
    current = (y + mid) * 100 // (x + mid)

    if current > z:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
