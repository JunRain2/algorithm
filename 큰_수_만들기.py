from itertools import combinations

def solution(number, k):
    numbers = list(number)
    comb = combinations(number, len(number) - k)
    
    nums = [int("".join(x)) for x in comb] 
    
    answer = str(max(nums))
    return answer