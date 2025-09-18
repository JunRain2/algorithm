import sys
input = sys.stdin.readline

S = input().strip()
n = len(S)

# 26개의 알파벳 각각에 대해 누적합 테이블 준비
# prefix[i][j] = 문자열 처음부터 j까지에서 (알파벳 i)가 나온 횟수
prefix = [[0] * (n + 1) for _ in range(26)]

for i in range(n):
    ch_idx = ord(S[i]) - ord('a')
    for j in range(26):
        prefix[j][i+1] = prefix[j][i]
    prefix[ch_idx][i+1] += 1

q = int(input())
out = []
for _ in range(q):
    c, l, r = input().split()
    l, r = int(l), int(r)
    idx = ord(c) - ord('a')
    # r+1까지 누적합에서 l까지 누적합 빼기
    out.append(str(prefix[idx][r+1] - prefix[idx][l]))

print("\n".join(out))
