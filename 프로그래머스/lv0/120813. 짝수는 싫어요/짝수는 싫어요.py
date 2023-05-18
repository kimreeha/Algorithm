def solution(n):
    answer = []
    while n != -1:
        if n % 2 == 0:
            n -= 1
        answer.append(n)
        n -= 2
    answer = sorted(answer)
    return answer