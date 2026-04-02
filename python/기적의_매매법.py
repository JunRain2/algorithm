"""
전량 매수와 전량 매도
- 현금 100원 주가 11원이라면 99원까지 매수


3일 연속 상승하는 주식 -> 다음 날 하락한다고 가정 -> 전량 매도

3일 연속 하락하는 주식 -> 다음 날 상승한다고 가정 -> 전량 매수

동일할 경우는 하락도 상승도 아님 -> 연속이 끊김
"""

a = b = int(input())
arr = list(map(int, input().split()))

# 각 주식 수
a_cnt = 0
b_cnt = 0

prev = arr[0]
down_cnt = 0
up_cnt = 0
for v in arr:
    # 전량 매수 
    a_cnt += a // v
    a = a % v
        
    if prev == v:
        down_cnt = 0
        up_cnt = 0
    elif prev > v:
        down_cnt += 1
        up_cnt = 0
    elif prev < v:
        down_cnt = 0
        up_cnt += 1
        
    if down_cnt >= 3:
        b_cnt += b // v
        b %= v
    if up_cnt >= 3:
        b += b_cnt * v
        b_cnt = 0
        
    prev = v
    
a += a_cnt * prev
b += b_cnt * prev

if a > b:
    print("BNP")
elif a < b:
    print("TIMING")
else:
    print("SAMESAME")