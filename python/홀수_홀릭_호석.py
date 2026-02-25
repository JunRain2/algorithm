# 수의 각 자리 숫자 중에서 홀수의 개수를 종이에 적는다.
def cnt_odd(num):
    arr = list(map(int,list(str(num))))
    
    result = 0
    for n in arr:
        result += n % 2 == 1
    
    return result

def dps(num):
    cnt = cnt_odd(num)
    # 한 자리
    if num < 10:
        return [cnt]
    
    # 두 자리일 경우 
    elif num < 100:
        # 두 개로 나눠서 새로운 값으로 더함
        a, b = map(int, list(str(num)))
        tmp =  dps(a + b)
        return [i + cnt for i in tmp]
        
    
    # 세 자리 이상일 경우
    else:
        nums = list(str(num))
        # 수가 세 자리 이상이면 임의의 위치에서 끊어서 세 개의 수로 분할하고, 3개를 더한 값을 새로운 수로 생각한다.
        
        result = []
        for i in range(1, len(nums)):
            for j in range(i + 1, len(nums)):
                a, b, c = int("".join(nums[:i])), int("".join(nums[i:j])), int("".join(nums[j::]))
                tmp =  dps(a + b + c)
                result.extend([x + cnt for x in tmp])
            
        return result
    

answer = dps(int(input()))
print(min(answer), max(answer))
