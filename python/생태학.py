import sys
from collections import Counter

arr = []
cnt = 0
for line in sys.stdin:
    arr.append(line.strip())

cnt = len(arr)    
counter = Counter(arr)

for k in sorted(counter):
    value = (counter[k] / cnt) * 100
    print(k, f"{value:.4f}")