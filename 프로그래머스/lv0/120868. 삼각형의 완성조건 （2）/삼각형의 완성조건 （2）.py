def solution(sides):
    highest = len([i for i in range(max(sides)+1) if i+min(sides)>max(sides)])
    rest = len([i for i in range(sum(sides)+1) if (max(sides)<i)&(sum(sides)>i)])
    return highest+rest