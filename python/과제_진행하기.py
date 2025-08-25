from collections import deque

def solution(plans):
    answer = []
    plans = sorted(plans, key = lambda x : x[1])

    # (이름, 남은 시간)
    delay = deque()
    for i in range(1, len(plans)):
        a = plans[i - 1]
        b = plans[i]
        
        duration = calcurate_duration(a[1], b[1])
        
        남은시간 = duration - int(a[2])
        if 남은시간 >= 0: # 남은 시간이 더 많거나 같은 경우
            answer.append(a[0])
            while(delay and 남은시간 > 0):
                # 남은 시간을 소모하면서 일을 처리
                name, time = delay.popleft()
                print(name, time, 남은시간)

                if 남은시간 >= time:
                    남은시간 -= time
                    answer.append(name)
                else:
                    time -= 남은시간
                    남은시간 = 0
                    delay.appendleft((name, time))
                       
        else:
            delay.appendleft((a[0], -남은시간))
      
    answer.append(plans[-1][0])
    for i in delay:
        answer.append(i[0])
    
    return answer

# a < b
def calcurate_duration(a, b):
    a_h, a_m = map(int, a.split(":"))
    b_h, b_m = map(int, b.split(":"))
    
    h = b_h - a_h
    return h * 60 + (b_m - a_m)