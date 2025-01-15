def solution(a, b, n):
    # a : 콜라 받기 위한 빈병 수, b : a개 갖다주면 주는 콜라 수, n : 빈병 개수
    answer = 0 # 받은 콜라 수
    new_coke = 0
    
    while n >= a:
        # print(n, new_coke, answer)
        new_coke = (n//a)*b # 새로 받은 콜라 수
               
        if n%a == 0:
            n = new_coke
        else:
            n = new_coke + n%a
        answer += new_coke # 빈병 a개 당 b개의 콜라 받음
    return answer