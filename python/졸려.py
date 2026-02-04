# 마지막 글자가 첫 번째 글자와 두 번째 글자 사이로 이동
# 뒤에서 두 번째 글자가 두 번째 글자와 세 번째 글자 사이로 이동
# 두에서 k번째 글자는 앞에서부터 k번째와 k+1번째 글자 사이로 이동 
# 위 단계를 역순으로 수행해야 함

x = int(input())
s = list(input())

original = s
history = [s] 

def shuffle(s):
    n = len(s)

    result = []
    tmp = []
    for i in range(n):
        if i % 2 == 1:
            tmp.insert(0, s[i])
        else: 
            result.append(s[i])
    
    return result + tmp    
    

cycle = 0
for i in range(1, x + 1):
    s = shuffle(s)
    if s == original: # 원래대로 돌아오면 주기 발견
        cycle = i
        break
    history.append(s)
    

if cycle > 0:
    print("".join(history[x % cycle]))
else:
    print("".join(s))