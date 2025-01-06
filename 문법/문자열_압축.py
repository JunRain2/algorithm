def solution(s):
    answer = 0

    min_length = len(s)

    for i in range(len(s)):  # 슬라이스 크기
        previous = ""
        data = dict()
        for j in range(len(s) - i):
            if previous == s[j : j + 1]:  # 이전 값과 현재 값 비교
                data[previous] += 1

        min_length = min(min_length, now_length)

    return answer
