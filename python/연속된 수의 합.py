def solution(num, total):
    # (num*(num-1))//2는 0부터 num-1까지의 합입니다.
    start = (total - (num * (num - 1) // 2)) // num
    # start부터 시작하는 num개의 정수를 리스트로 반환합니다.
    return list(range(start, start + num))