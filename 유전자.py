s = list(input())

"""
at와 gc는 가장 짧은 길이의 KOI 유전자
어떤 X가 KOI 유전자라면, aXt와 gXc도 KOI 유전자
어떤 X와 Y가 KOI 유전자라면 둘을 연결한 XY도 KOI 유전자
"""

n = len(s)
stack = []

result = 0
for i in range(n):
    if not stack:
        stack.append(s[i])
        continue

    if "a" in stack and s[i] == "t":
        result += 2
        while stack[-1] != "a":
            stack.pop()
        stack.pop()
    elif "g" in stack and s[i] == "c":
        result += 2
        while stack[-1] != "g":
            stack.pop()
        stack.pop()
    else:
        stack.append(s[i])

print(result)
