def solution(chicken):
    answer = 0
    for i in range(chicken):
        answer += chicken//10
        chicken = chicken%10 + chicken//10
    return answer