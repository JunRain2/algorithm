def solution(s):
    answer = 0
    
    s = list(s)
    n = len(s)
    for start in range(n):
        stack = []
        for i in range(n):
            current = (start + i) % n
            if s[current] == "]" or s[current] == ")" or s[current] == "}":
                if not stack:
                    stack.append(".")
                    break
                if (stack[-1] == "[" and s[current] == "]") or (stack[-1] == "(" and s[current] == ")") or (stack[-1] == "{" and s[current] == "}"):
                    stack.pop()
                else: # 짝이 안맞는 경우
                    stack.append(".")
                    break
            else:
                stack.append(s[current])
                
        print(stack)        
        answer += not stack
                
    return answer