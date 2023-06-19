def solution(score):
    mean = [sum(i)/2 for i in score]
    avg_rank = sorted(mean)[::-1]
    return [avg_rank.index(i)+1 for i in mean]