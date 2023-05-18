def solution(array):
    answer = []
    n_dict = {}
    for i in array:
        n_dict[i] = 0

    for k in n_dict:
        for i in array:
            if i == k:
                n_dict[k] += 1
    for k in n_dict:
        if n_dict[k] == max(list(n_dict.values())):
            answer.append(k)
    if len(answer) > 1:
        return -1
    else:
        return answer[0]