from collections import Counter

for tc in range(int(input())):
    w = list(input())
    n = len(w)
    k = int(input())
    result = []

    flag = False
    for i in range(k, n):
        for j in range(0, n - i):
            counter = Counter(w[j:j + i])
            if k == counter.most_common(1)[0][1]:
                result.append(i)
                flag = True
                break
        if flag:
            break
        
    if not flag:
        print(-1)
        break
    
    answer = result[0]
    for i in range(k, n):
        for j in range(0, n - i):
            if w[j] != w[j + i - 1]:
                continue
            counter = Counter(w[j:j + i])
            if k == counter[w[j]]:
                answer = max(answer, i)
    
    result.append(answer)
    print(*result)