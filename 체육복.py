# 전체 학생의 수, 도난 당한 학생들의 번호, 여벌의 체육복을 가져온 학생
def solution(n, lost, reserve):
    n -= len(lost)
    tmp = set(lost) & set(reserve)

    for t in tmp:
        reserve.remove(t)
        lost.remove(t)
        n += 1

    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
            n += 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            n += 1
            
    return n