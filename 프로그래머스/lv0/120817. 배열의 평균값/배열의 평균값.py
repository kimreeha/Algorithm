def solution(numbers):
    cnt = 0
    for i in numbers:
        cnt += i
    answer = cnt / len(numbers)
    return answer