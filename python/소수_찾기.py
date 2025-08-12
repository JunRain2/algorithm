from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = 0
    numbers_set = set()
    
    for i in range(1, len(numbers) + 1):
        for j in permutations(list(numbers), i):
            numbers_set.add(int("".join(j)))
    
    numbers = list(numbers_set)
    for num in numbers:
        answer += is_prime(num)
            
    return answer