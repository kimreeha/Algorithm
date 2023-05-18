def solution(numbers):
    n = sorted(numbers)
    answer = n[-1]*n[-2]
    return answer