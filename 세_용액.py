n = int(input().strip())
arr = list(map(int, input().split()))
arr.sort()

best_sum = int(4e9)
answer = [0, 0, 0]

for i in range(n - 2):
    left = i + 1
    right = n - 1
    
    while left < right:
        current_sum = arr[i] + arr[left] + arr[right]
        
        # 0에 가까운 합인지 업데이트
        if abs(current_sum) < abs(best_sum):
            best_sum = current_sum
            answer = [arr[i], arr[left], arr[right]]
            # 합이 정확히 0이면 더 이상 개선 불가하므로 바로 출력 후 종료
            if best_sum == 0:
                print(*sorted(answer))
                exit()
        
        # 합이 음수면 왼쪽 포인터를 오른쪽으로 이동하여 값을 키운다.
        if current_sum < 0:
            left += 1
        # 합이 양수면 오른쪽 포인터를 왼쪽으로 이동하여 값을 줄인다.
        else:
            right -= 1

print(*sorted(answer))