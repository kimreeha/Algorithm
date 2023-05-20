def solution(money):
    max_num = money // 5500
    rest_money = money % 5500
    answer = [max_num, rest_money]
    return answer