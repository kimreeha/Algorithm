def solution(my_str, n):
    answer = [my_str[n*i:n*(i+1)] for i in range(len(my_str)) if len(my_str) > n*i]
    return answer