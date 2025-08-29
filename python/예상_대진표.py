"""
1, 2 와 같이 배정

8, 4, 7
8명 중에 4번과 7번이 맞붙었을 때 몇 번째에서 맞붙게 되는가?
"""

import math


def solution(n, a, b):
    start, end = 1, n

    answer = int(math.log2(n))

    while start <= end:
        mid = (start + end) // 2

        # 중심축을 기준으로 서로 반대일 경우
        if (mid < a <= end and start <= b <= mid) or (
            start <= a <= mid and mid < b <= end
        ):
            return answer
        # 중심축의 오른쪽에 몰려있을 경우
        elif mid < a <= end and mid < b <= end:
            start = mid + 1
            answer -= 1
        else:
            end = mid
            answer -= 1

    return answer
