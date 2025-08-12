n, k = map(int, input().split())

cnt = 0

while True:
    # k로 나눌 수 있게 n을 맞추는 과정
    target = (n // k) * k # 나눌 수 있는 값을 찾음
    cnt += (n - target) # 나눌 수 있는 값으로 조정하는 과정
    n = target
    
    # 더 이상 나눌 수 없을 때
    if n < k:
        break
    
    cnt += 1
    n //= k

cnt += (n - 1)
print(cnt)
