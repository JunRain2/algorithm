n = int(input())
heights = list(map(int, input().split()))
result = [0] * n

# 키가 작은 사람부터 차례대로 배치
for i in range(n):
    cnt = 0  # 빈자리 카운트
    for j in range(n):
        # 빈자리를 발견하면 카운트 증가
        if result[j] == 0:
            cnt += 1
            # 필요한 빈자리 수에 도달하면 현재 사람을 배치
            if cnt == heights[i] + 1:
                result[j] = i + 1
                break

print(*result)
