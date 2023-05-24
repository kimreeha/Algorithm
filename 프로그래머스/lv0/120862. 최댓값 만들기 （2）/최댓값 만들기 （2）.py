def solution(numbers):
    numbers = sorted(numbers, reverse = True)
    plus = numbers[0]*numbers[1]
    minus = numbers[-1]*numbers[-2]
    if plus > minus:
        answer = plus
    else:
        answer = minus
    return answer