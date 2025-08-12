n, m = map(int, input().split())

array = list()

for _ in range(n):
    array.append(int(input()))

# min()을 통해서 비교해야 하기 때문에 m의 최댓값을 넘어선 10001로 설정
d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001: #d[0] = 0이기 때문에 첫 번째 값이 패스될 일은 없다.
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])