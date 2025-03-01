import math

# 소시지 수, 평론가의 수
n, m = map(int, input().split())

# 
a, b = divmod(n, m)

if b == 0:
    print(0)
else:
    if b == 1:
        print(m - 1)
    else:
        print(m - math.gcd(b, m))
        
"""
4명일 때 2조각 -> 2번 자름
6명일 때 2조각 -> 4번 자름
4명일 때 3조각 -> 3번 자름
"""