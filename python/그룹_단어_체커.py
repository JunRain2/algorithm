n = int(input())

answer = 0
for _ in range(n):
    chars = list(input())
    
    prev = chars[0]
    exists = set(prev)
    flag = True
    for c in chars:
        # 이전과 동일할 때 -> 그룹
        if c == prev:
            continue
        
        # 이전과 단어가 달라졌을 때
        if c in exists:
            flag = False
            break
        
        prev = c
        exists.add(c)
    
    answer += flag
    
print(answer)