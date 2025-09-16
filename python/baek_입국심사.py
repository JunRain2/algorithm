n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

left, right = 1, max(arr) * m
answer = right

while left <= right:
    mid = (left + right) // 2
    people = 0
    
    for t in arr:
        people += mid // t
        if people >= m:  # 이미 m명 이상이면 더 계산할 필요 없음
            break
    
    if people >= m:  # mid 시간 안에 다 처리 가능 → 더 줄여본다
        answer = mid
        right = mid - 1
    else:  # mid 시간으론 부족 → 시간을 늘린다
        left = mid + 1

print(answer)
