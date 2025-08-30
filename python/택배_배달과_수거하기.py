"""
n개의 집에 택배를 배달
트럭에 cap개까지 실을 수 있다.
각 집에 배달 및 수거할 때, 원하는 개수만큼 택배를 배달 및 수거할 수 있다.

몇 번 왕복하고 나머지를 어떻게 할래?
"""
def solution(cap, n, deliveries, pickups):
    answer = 0
    
    send_point = []
    send_capacity = cap
    
    return_point = []
    return_capacity = cap
    
    for current in range(n - 1, -1, -1):
        # 보낼 때 어디까지 몇 번 왔다갔다 해야하는지
        if send_capacity == cap and deliveries[current] != 0:
            send_point.append(current)
            
        if send_capacity - deliveries[current] >= 0:
            send_capacity -= deliveries[current]
        else:
            # cap은 3인데 9개를 배달해야하는 경우
            deliveries[current] -= send_capacity
            div, mod = divmod(deliveries[current], cap)
            
            cnt = div + (1 if mod != 0 else 0)
            for i in range(cnt):
                send_point.append(current)
                
            send_capacity = cap - mod
            
        # 수거할 때 몇 번 왔다갔다 해야하는지
        if return_capacity == cap and pickups[current] != 0:
            return_point.append(current)
            
        if return_capacity - pickups[current] >= 0:
            return_capacity -= pickups[current]
        else:
            pickups[current] -= return_capacity
            div, mod = divmod(pickups[current], cap)
            
            cnt = div + (1 if mod != 0 else 0)
            for i in range(cnt):
                return_point.append(current)
                
            return_capacity = cap - mod
            
            
    for i in range(max(len(return_point), len(send_point))):
        if i >= len(return_point):
            answer += (send_point[i] + 1) * 2
        elif i >= len(send_point):
            answer += (return_point[i] + 1) * 2
        else:
            반환점 = max(return_point[i], send_point[i]) + 1
            answer += 반환점 * 2    
        
    return answer