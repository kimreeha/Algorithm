def solution(s):
    dict_s, answer = dict.fromkeys(s,0), ''
    for i in s:
        if i in dict_s:
            dict_s[i] += 1
    for k,v in dict_s.items():
        if v < 2:
            answer += k
    return ''.join(sorted(answer))