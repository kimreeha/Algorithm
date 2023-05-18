def solution(num_list):
    cnt, cnt1 = 0, 0
    for i in num_list:
        if i % 2 == 0:
            cnt += 1
        else:
            cnt1 += 1
    answer = [cnt, cnt1]
    return answer