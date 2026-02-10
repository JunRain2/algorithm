s = list(input())
t = list(input())

"""
반대로 t를 s로 변환해보자
"""

def execute(t):
    # A만 추가됐던 것이기 때문에 A를 제거
    last = t.pop()
    if last == 'A':
        return t
    
    return list(reversed(t))

while len(s) < len(t):
    t = execute(t)
    
print(int(s == t))