def solution(my_string):
    answer = ''
    cnt = {}
    for i in my_string:
        cnt[i] = 0
    for i in my_string:
        cnt[i] += 1
        if cnt[i] < 2:
            answer += i
    return answer