def solution(array):
    n_array = sorted(array)
    i = len(n_array)
    if i % 2 == 0:
        answer = (n_array[i//2] + n_array[i//2-1])/2
    else:
        answer = n_array[i//2]
    return answer