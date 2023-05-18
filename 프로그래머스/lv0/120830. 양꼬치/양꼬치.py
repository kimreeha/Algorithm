def solution(n, k):
    answer = n*12000 + 2000*(k - n//10)
    return answer