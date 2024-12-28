n, m, k = map(int, input().split())
arr = list(map(int, input().split()))[:n]

arr.sort()
first = arr[n - 1]
second = arr[n - 2]

result = 0

while True:
    # k만큼 first를 반복해서 더한 후, second를 한 번 더함
    # 위 행위를 while문에서 반복
    for i in range(k):
        if m == 0:
            break;
    result += first
    m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)