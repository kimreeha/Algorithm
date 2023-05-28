def solution(s):
    lst = list(s.split(' '))
    cnt = 0
    for i in range(len(lst)):
        if lst[i] == 'Z':
            cnt -= int(lst[i-1])
        else:
            cnt += int(lst[i])
    return cnt