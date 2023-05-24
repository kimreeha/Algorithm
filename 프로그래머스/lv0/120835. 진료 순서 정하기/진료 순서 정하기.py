def solution(emergency):
    answer = []
    sort = {}
    cnt = 1
    emer = sorted(emergency, reverse = True)
    for i in emer:
        sort[i] = cnt
        cnt += 1
    for i in emergency:
        if i in sort:
            answer.append(sort[i])
    return answer