import itertools

def solution(number):
    answer = 0
    lst = list(itertools.combinations(number, 3))
    
    for i in lst:
        if sum(i) == 0:
            answer+=1
    return answer