array = list(input())

stack = result = 0
flag = False

for i in array:
    if i == "(":
        stack += 1
        flag = True
    elif i == ")":
        if flag:
            stack -= 1
            result += stack
            flag = False
        elif not flag:
            stack -= 1
            result += 1


result += stack
print(result)
        