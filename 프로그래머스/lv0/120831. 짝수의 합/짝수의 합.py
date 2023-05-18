def solution(n):
    answer = 0
    array = []
    while n > 0:
        if n % 2 == 0:
            array.append(n)
        else:
            n -= 1
            array.append(n)
        n -= 2
    for i in array:
        answer += i
    return answer