def solution(name):
    n = len(name)
    answer = 0
    
    # 1. 각 문자별 상하 조작 횟수 합산
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    # 2. 좌우 이동 최소 횟수 계산
    # 기본적으로 오른쪽으로 모두 이동하는 경우 (n-1) 이동을 가정
    move = n - 1
    
    # i: 현재까지 오른쪽으로 이동한 인덱스
    # j: i 이후 연속된 'A' 구간이 끝나는 지점
    for i in range(n):
        j = i + 1
        while j < n and name[j] == 'A':
            j += 1
        # 두 가지 경우를 모두 고려하여 최소값 선택
        # 1) 오른쪽으로 i칸 이동 후, 왼쪽으로 돌아서 나머지 (2*i + n - j)
        # 2) 오른쪽으로 i칸 이동 후, 다시 오른쪽으로 (i + 2*(n - j))
        move = min(move, 2*i + n - j, i + 2*(n - j))
    
    answer += move
    return answer
