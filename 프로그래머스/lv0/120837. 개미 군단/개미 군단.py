def solution(hp):
    answer = 0
    ants = [5,3,1]
    for i in ants:
        answer += hp // i
        hp %= i
    return answer