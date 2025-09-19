n = int(input())  # 이동하려는 채널
m = int(input())  # 고장난 버튼 수
broken = set(map(int, input().split())) if m else set()
usable = {i for i in range(10)} - broken

# +, - 만으로 이동하는 경우
ans = abs(n - 100)

# 숫자 버튼으로 가능한 모든 채널 탐색
for c in range(1000000):  # 충분히 큰 범위까지
    s = str(c)
    if all(int(ch) in usable for ch in s):  # 모든 자리 눌러도 되는지 확인
        press = len(s) + abs(c - n)  # 숫자 입력 횟수 + 차이
        ans = min(ans, press)

print(ans)