# 인용 횟수를 담은 citations
# mid를 기준으로 탐색
# mid값이 h이상이면서, h개가 남아있어야 함
def solution(citations):
    answer = 0
    citations.sort()

    start = 0
    end = len(citations) - 1
    while start <= end:
        mid = (start + end) // 2
        h = len(citations) - mid

        # 남은 인덱스와 현재 인덱스의 번호가
        if h <= citations[mid]:
            answer = h
            end = mid - 1
        else:
            start = mid + 1

    return answer
