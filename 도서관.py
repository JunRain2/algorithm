n, m = map(int, input().split())
array = list(map(int, input().split()))

if n == 1:
    print(abs(array[0]))
    exit()

p_array = [i for i in array if i > 0]
p_array.append(0)
p_array.sort(reverse=True)

n_array = [i for i in array if i < 0]
n_array.append(0)
n_array.sort()

result = 0
if abs(min(n_array)) > max(p_array):
    result += abs(n_array[0])
    n_array = n_array[m:]
else:
    result += p_array[0]
    p_array = p_array[m:]

for i in range(0, len(p_array), m):
    result += p_array[i] * 2

for j in range(0, len(n_array), m):
    result += abs(n_array[j]) * 2

print(result)
