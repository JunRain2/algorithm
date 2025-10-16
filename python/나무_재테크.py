from collections import defaultdict

n, m, k = map(int, input().split())
nour = [list(map(int, input().split())) for _ in range(n)]
land = [[5] * n for _ in range(n)]

# 각 칸별로 나무를 관리 (정렬된 리스트로)
trees_map = defaultdict(list)

for _ in range(m):
    x, y, z = map(int, input().split())
    trees_map[(x-1, y-1)].append(z)

# 각 칸의 나무들을 나이순으로 정렬
for key in trees_map:
    trees_map[key].sort()

def simulate_year():
    new_trees_map = defaultdict(list)
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for (x, y), ages in trees_map.items():
        alive = []
        dead_nutrient = 0
        
        # 봄: 어린 나무부터 양분 먹기 (이미 정렬됨)
        for age in ages:
            if land[x][y] >= age:
                land[x][y] -= age
                new_age = age + 1
                alive.append(new_age)
                
                # 가을: 번식 (나이가 5의 배수)
                if new_age % 5 == 0:
                    for i in range(8):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            new_trees_map[(nx, ny)].append(1)
            else:
                # 여름: 죽은 나무는 양분으로
                dead_nutrient += age // 2
        
        # 여름: 양분 추가
        land[x][y] += dead_nutrient
        
        # 살아있는 나무가 있으면 저장
        if alive:
            new_trees_map[(x, y)].extend(alive)
    
    # 겨울: 양분 추가
    for x in range(n):
        for y in range(n):
            land[x][y] += nour[x][y]
    
    # 각 칸의 나무들을 나이순으로 정렬
    for key in new_trees_map:
        new_trees_map[key].sort()
    
    return new_trees_map

for _ in range(k):
    trees_map = simulate_year()

# 전체 나무 개수 계산
total = sum(len(ages) for ages in trees_map.values())
print(total)