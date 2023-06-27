def solution(a, b):
    c = sorted([a,b])
    return sum([i for i in range(c[0],c[1]+1)])