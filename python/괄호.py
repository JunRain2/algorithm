from collections import deque

def check(str):
    stack = deque()
    
    for s in str:
        if len(stack) == 0:
            if s == "(":
                stack.append(s)
            elif s == ")":
                return "NO"
        elif stack[-1] == "(":
            if s == "(":
                stack.append(s)
            elif s == ")":
                stack.pop()
                
    if stack:
        return "NO"
    
    return "YES"
    

for tc in range(int(input())):
    arr = list(input())
    print(check(arr))
        
"""
peek -> empty
    ( -> 추가
    ) -> "NO" 하고 종료

peek -> ( 
    (  -> 스택에 추가
    ) -> pop
"""