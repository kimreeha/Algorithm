def solution(balls, share):
    a, b, c = 1, 1, 1
    for i in range(2, balls+1):
        a *= i
    for i in range(2, balls-share+1):
        b *= i
    for i in range(2, share+1):
        c *= i
    answer = a / (b*c)
    return answer