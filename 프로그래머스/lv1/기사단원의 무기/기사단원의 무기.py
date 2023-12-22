def solution(number, limit, power):
    # 1. 약수의 개수를 반환하는 리스트 생성
    # 2. 약수 리스트를 순회하며 limit를 넘는경우, 해당 원소를 제거하고 power를 삽입
    # 3. 약수 리스트의 총합 반환
    def divisor(number):
        cd = []
        for i in range(1, int(number**(1/2))+1):
            if number%i==0:
                cd.append(i)
                if i < number//i:
                    cd.append(i)
        return cd

    cd_lst = []
    answer = 0
    
    for i in range(1, number+1):
        cnt = 0
        cd = divisor(i)
        cd_lst.append(len(cd))
        
    for i in cd_lst:
        if i > limit:
            answer += power
            continue
        answer += i
    
    return answer