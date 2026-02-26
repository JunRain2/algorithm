import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memos = set()
for _ in range(n):
    memos.add(input().rstrip())

for _ in range(m):
    words = set(input().rstrip().split(','))
    memos.difference_update(words) # 다른 set의 원소들을 제저라에서 제거
    print(len(memos)) 