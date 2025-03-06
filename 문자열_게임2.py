from collections import defaultdict

for _ in range(int(input())):
    w = input()
    k = int(input())
    
    if k > len(w):
        print(-1)
        continue
    
    char_positions = defaultdict(list)
    for i, char in enumerate(w):
        char_positions[char].append(i)
    
    min_len = float('inf')
    max_len = -1
    
    for char, positions in char_positions.items():
        if len(positions) >= k:
            for i in range(len(positions) - k + 1):
                length = positions[i+k-1] - positions[i] + 1
                min_len = min(min_len, length)
                max_len = max(max_len, length)
    
    if min_len == float('inf') or max_len == -1:
        print(-1)
    else:
        print(min_len, max_len)
