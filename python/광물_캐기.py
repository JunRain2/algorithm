"""
최소한의 피로도를 통해 광물을 캘 예정

곡괭이는 5번 사용할 수 있다.
한 번 선택 -> 사용할 수 없을 때까지
광물은 주어진 순서대로 -> 다이아가 고벨류
광산에 있는 모든 광물을 캐거나, 더 사용할 곡갱이가 없을 때까지 광물을 캔다.


그리드로 풀 것인가 dp로 풀 것인가?
"""

from collections import Counter


# 곡괭이 개수를 나타내는 정수 배열, 광물의 순서를 나타내는 문자 배열
def solution(picks, minerals):
    minerals = minerals[: sum(picks) * 5]
    minerals = [Counter(minerals[i : i + 5]) for i in range(0, len(minerals), 5)]
    minerals = [[m["diamond"], m["iron"], m["stone"]] for m in minerals]
    minerals = list(
        reversed(sorted(minerals, key=lambda x: x[0] * 25 + x[1] * 5 + x[2] * 1))
    )

    print(minerals)

    answer = 0
    i = 0
    for m in minerals:
        print(m)
        while picks[i] == 0:
            i += 1

        for j in range(3):
            answer += m[j] * score[i][j]

        picks[i] -= 1

    return answer


score = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
