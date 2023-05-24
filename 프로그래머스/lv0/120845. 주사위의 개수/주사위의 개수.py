def solution(box, n):
    answer = 1
    for i in box:
        nn = i // n
        answer *= nn
    return answer