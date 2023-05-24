def solution(rsp):
    answer = ''
    victory = {'2':'0', '0':'5', '5':'2'}
    for i in rsp:
        if i in victory:
            answer += victory[i]
    return answer