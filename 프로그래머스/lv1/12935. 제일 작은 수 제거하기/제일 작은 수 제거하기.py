def solution(arr):
    answer = [i for i in arr]
    answer.remove(min(arr))
    if len(answer) == 0:
        return [-1]
    else:
        return answer