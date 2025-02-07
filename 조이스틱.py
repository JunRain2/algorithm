def solution(name):
    answer = 0
    tmp = ['A'] * len(name)
    direction = 0
    
    # 방향은 맨 처음에 결정 -> 중간에 변경되면 왔던 길을 되돌아가 최솟값이 나오지 않음
    if name.find('A') == -1 or name[-1] == 'A':
        direction = 1
    else:
        direction = -1
        
    name = list(name)
    index = 0
    while True:
        a = name[index]
        answer += min((ord('Z') - ord(a) + 1, ord(a) - ord('A')))
        tmp[index] = name[index]
        
        if tmp == name:
            break
    
        index = (index + direction) % len(name)
        answer += 1 # tmp와 name이 같으면 옮기지 않아도 되기 때문에
    

    return answer