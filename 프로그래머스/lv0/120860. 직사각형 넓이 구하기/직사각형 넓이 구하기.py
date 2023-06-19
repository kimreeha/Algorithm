def solution(dots):
    x = max([dots[i][0] for i in range(4)]) - min([dots[i][0] for i in range(4)])
    y = max([dots[i][1] for i in range(4)]) - min([dots[i][1] for i in range(4)])
    return x*y