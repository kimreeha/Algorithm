def solution(sides):
    return len([i for i in range(max(sides)+1) if i+min(sides)>max(sides)]) + len([i for i in range(sum(sides)+1) if (max(sides)<i)&(sum(sides)>i)])
