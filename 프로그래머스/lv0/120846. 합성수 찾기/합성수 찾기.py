def solution(n):
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        for v in range(1, i+1):
            if i % v == 0:
                cnt += 1
        if cnt >= 3:
            answer += 1
    return answer