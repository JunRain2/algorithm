n, m = map(int, input().split())

websites = dict()
for _ in range(n):
    web, pwd = input().split()
    websites[web] = pwd
    
for _ in range(m):
    print(websites[input()])