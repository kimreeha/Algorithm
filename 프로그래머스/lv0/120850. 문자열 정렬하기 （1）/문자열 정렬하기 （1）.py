def solution(my_string):
    answer = []
    nums = ('1','2','3','4','5','6','7','8','9','0')
    for i in my_string:
        if i in nums:
            answer.append(int(i))
    answer.sort()
    return answer