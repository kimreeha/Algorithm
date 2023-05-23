def solution(n):
    m = str(n)
    answer = 0
    lst = []
    for i in m:
        lst.append(int(i))
    for v in lst:
        answer += v
    return answer