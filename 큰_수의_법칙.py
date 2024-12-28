n, m, k = map(int, input().split())
arr = list(map(int, input().split()))[:n]

arr.sort(reverse=True)
first = arr[0]
second = arr[1]

count = int(m / (k+1)) * k # first가 등장하는 횟수
count += m % (k+1) # 수가 정확하게 나누어 떨어지지 않았을 경우, 나머지를 더함

result = 0
result += (count)* first
result += (m-count) * second

print(result)