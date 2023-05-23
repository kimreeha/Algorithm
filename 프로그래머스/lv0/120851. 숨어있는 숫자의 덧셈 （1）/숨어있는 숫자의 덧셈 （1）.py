def solution(my_string):
    answer = 0
    lst = ('1','2','3','4','5','6','7','8','9')
    lst_n = []
    for i in my_string:
        if i in lst:
            lst_n.append(int(i))
    for v in lst_n:
        answer += v
    return answer