n = int(input())
array = [input() for _ in range(n)]

a = set()

result = []
for i in array:
    s = i.split()
    flag = False

    st = []
    for j in s:
        if j[0].upper() not in a and not flag:
            flag = True
            a.add(j[0].upper())
            j = "[" + j[0] + "]" + j[1:]
        st.append(j)
        st.append(" ")

    if not flag:
        st = []
        for j in s:
            for k in range(len(j)):
                if j[k].upper() not in a and not flag:
                    a.add(j[k].upper())
                    flag = True
                    j = j[:k] + "[" + j[k] + "]" + j[k + 1 :]
                    
            st.append(j)
            st.append(" ")

    result.append("".join(st).rstrip())

for i in result:
    print(i)
