n = int(input())

arr = [int(input()) for _ in range(n)]

# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때
# 각각이 로프에는 모두 고르게 w/k 만큼의 중량이 걸림
arr.sort()

result = 0
for i, v in enumerate(arr):
    result = max(result, v * (n - i))
    
print(result)