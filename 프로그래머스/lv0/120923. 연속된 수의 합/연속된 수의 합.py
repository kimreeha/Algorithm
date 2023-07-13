def solution(num, total):
    answer = [i for i in range(-1000, 1000)]
    for i in range(len(answer)):
        while sum(answer[i:i+num]) == total:
            return answer[i:i+num]
        