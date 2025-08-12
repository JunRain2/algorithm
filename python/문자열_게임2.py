from collections import defaultdict

for tc in range(int(input())):
    s = list(input())
    k = int(input())
    
    d = defaultdict(list)
    for i, c in enumerate(s):
        d[c].append(i)
    
    result1 = int(1e9)
    result2 = -1
    for i in d.keys():
        if len(d[i]) < k:
            continue
        for j in range(len(d[i]) - k + 1):
            result1 = min(result1, d[i][j + k - 1] - d[i][j] + 1)
            result2 = max(result2, d[i][j + k - 1] - d[i][j] + 1)
    
    if result1 == int(1e9):
        print(-1)
    else:
        print(result1, result2)