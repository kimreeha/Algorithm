def solution(food):
    answer = ''
    food_num = [str(i) for i in range(len(food))]
    
    for i in range(1,len(food)):
        answer += food_num[i]*(food[i]//2)
    answer_re = answer[::-1]
    answer += '0'
    return answer + answer_re