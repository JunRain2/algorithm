from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    start = [0] * (len(truck_weights) + 1)
    end = [0] * (len(truck_weights) + 1)
    
    start_index = 1
    end_index = 1
    q = deque()
    for truck in truck_weights:
        sum_t, len_t = sum(q) + truck, len(q) + 1
        while sum_t > weight or len_t > bridge_length:
            sum_t -= q.popleft()
            len_t -= 1
            end[end_index] = start[end_index] + bridge_length
            end_index += 1
        q.append(truck)
        start[start_index] = end[end_index - 1] + 1
    
    return max(end)