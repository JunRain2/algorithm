n = int(input().strip())
seq = list(map(int, input().split()))

# 1. n이 1인 경우
if n == 1:
    print("A")
    exit()

# 2. n이 2인 경우
if n == 2:
    if seq[0] == seq[1]:
        print(seq[0])
    else:
        print("A")
    exit()

# 3. n이 3 이상인 경우

# (1) 첫 두 항이 같은 경우
if seq[0] == seq[1]:
    # 첫 두 항이 같으면서 전체가 상수열인지 확인
    all_same = True
    for x in seq:
        if x != seq[0]:
            all_same = False
            break
    if all_same:
        print(seq[0])
        exit()
    else:
        print("B")
        exit()

# (2) 첫 세 항을 이용해 a와 b 계산
diff1 = seq[1] - seq[0]
diff2 = seq[2] - seq[1]

# a는 diff2 / diff1이어야 함 (정수여야 함)
if diff1 == 0 or diff2 % diff1 != 0:
    print("B")
    exit()

a = diff2 // diff1
b = seq[1] - a * seq[0]

# (3) 전체 수열 검증
valid = True
for i in range(n - 1):
    if seq[i + 1] != a * seq[i] + b:
        valid = False
        break

if not valid:
    print("B")
else:
    # 다음 항 계산
    print(a * seq[-1] + b)
