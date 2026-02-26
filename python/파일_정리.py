from collections import defaultdict

n = int(input())

extensions = defaultdict(int) # 0으로 초기화
for _ in range(n):
    _, extension = input().split('.')
    extensions[extension] += 1
    
for k in sorted(extensions.keys()):
    print(k, extensions[k])
    