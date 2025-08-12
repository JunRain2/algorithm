s = list(map(int, input()))

now = s[0]
cnt1 = 0
cnt0 = 0

if now == 1:
    cnt1+= 1
else:
    cnt0+= 1

for i in range(1, len(s)):
    if now == s[i]:
        continue
    else:
        now = s[i]
        if s[i] == 0:
            cnt0 += 1
        else:
            cnt1 += 1
    
    
print(min(cnt1, cnt0))