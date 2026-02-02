

gens = dict()
dels = []

target = None

while True:
    i = input().split()
    command, etc = i[0], i[1::]
    
    if command == "gen:":
        gens[etc[0]] = etc[-1]
    elif command == "del:":
        dels.append(list(etc[0]))
    elif command  == "target:":
        target = etc[0]
        break
        
def execute_gen(arr):
    result = []
    
    for s in arr:
        if s in gens.keys(): # 생성 명령어가 존재하는 경우
            result.extend(gens[s])
        else: # 생성 명령어가 존재하지 않는 경우
            result.append(s)
    
    return result    

def execute_del(arr):
    """
    AAABA -> BA
    패턴 맞추기가 필요한데...
    """
    if not dels:
        return arr
    
    index = set(range(len(arr)))
    for i in range(len(arr)):
        for d in dels:
            n = len(d)
            if arr[i:min(i+n, len(arr))] == d:
                for i in range(i, i + n):
                    if i in index:
                        index.remove(i)
    
    index = sorted(list(index))
    result = []
    for i in index:
        result.append(arr[i])
    
    return result
                

codes = ['A']
# 10번동안 진행
for _ in range(10):
    codes = execute_gen(codes)
    codes = execute_del(codes)
    
    if target == "".join(codes):
        break


print("O" if target == "".join(codes) else "X")