def solution(dot):
    x, y = dot[0], dot[1]
    if (x>0) & (y>0):
        answer = 1
    elif (x<0) & (y>0):
        answer = 2
    elif (x<0) & (y<0):
        answer = 3
    else:
        answer = 4
    return answer