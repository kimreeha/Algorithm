def solution(numbers, k):
    lst = [i for i in numbers]*k
    return [lst[i*2] for i in range(k)][-1]