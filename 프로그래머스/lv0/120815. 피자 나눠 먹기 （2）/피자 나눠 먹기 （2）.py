def solution(n):
    array = [n, n*2, n*3, n*6]
    for i in array:
        if i % 6 == 0:
            return i // 6