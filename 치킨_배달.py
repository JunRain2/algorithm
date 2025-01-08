n, m = map(int, input().split())

chicken = list()
home = list()

# 치킨집과 집을 좌표로 도식화
for i in range(1, n + 1):
    data = list(map(int, input().split()))[:n]
    for j in range(n):
        if data[j] == 0:
            continue
        elif data[j] == 1:
            home.append((i, j + 1))
        elif data[j] == 2:
            chicken.append((i, j + 1))
            
array = list()
for c in home:
    c_x, c_y = c
    a = list()
    for h in home:
        h_x, h_y = h
        a.append(abs(h_x - c_x) + abs(h_y - c_y))
    array.append(a)
    

print(sum(array))