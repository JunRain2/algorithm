from itertools import product

def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    dictionary = set()
    for i in range(1, 6):
        for j in product(words, repeat = i):
            dictionary.add("".join(j))
            
    dictionary = list(dictionary)
    dictionary.sort()
    
    return dictionary.index(word) + 1