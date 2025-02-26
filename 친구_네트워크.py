for tc in range(int(input())):
    f = int(input())
    result = []
    
    for _ in range(f):
        a, b = input().split()
        # a의 집합과 b의 집합을 합친 후 크기를 반환하는 문제
        # a와 b의 집합을 찾음 -> a와 b집합을 합침
        a_set = None
        b_set = None
        for i in result:
            if a in i:
                a_set = i
                a_set.add(b)
            if b in i:
                b_set = i
                b_set.add(a)
                
        if a_set == None:
            a_set = set()
        else:
            result.remove(a_set)
        if b_set == None:
            b_set = set()
        elif b_set in result:
            result.remove(b_set)
            
        a_set.add(b)
        b_set.add(a)
        
        total_set = a_set | b_set
        result.append(total_set)
        print(len(total_set))
        
        