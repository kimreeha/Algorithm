def solution(numbers):
    lst = [i for i in range(0,10)]
    answer = 0
    for i in lst:
        if i not in numbers:
            answer += i
    return answer