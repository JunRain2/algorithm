def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    current = 0
    while True:
        if k == 0:
            break
            
        current %= len(food_times)  
        
        if food_times[current] == 0:
            current += 1
            continue
        
        k -= 1
        food_times[current] -= 1
        current += 1
    
    return current % len(food_times) + 1