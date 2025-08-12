def solution(sizes):
    answer = max(max(x) for x in sizes) * max(min(x) for x in sizes)
    return answer
