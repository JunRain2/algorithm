n = int(input())

data = list()
for _ in range(n):
    name, a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    data.append((a, b, c, name))


def sort_student(s1, s2):
    if s1[0] != s2[0]:
        return s1[0] - s2[0]  # 국어 내림차순
    else:
        if s1[1] != s2[1]:
            return s2[1] - s1[1]  # 영어 오름차순
        else:
            if s1[2] != s2[2]:
                return s1[2] - s2[2]  # 수학 내림차순
            else:
                return s2[3] - s1[3]  # 이름 오름차순


data.sort(sort_student)

for i in data:
    print(i[3])
