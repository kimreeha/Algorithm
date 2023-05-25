def solution(array):
    answer = []
    ord_array = sorted(array)
    answer.append(ord_array[-1])
    for i in range(len(array)):
        if array[i] == ord_array[-1]:
            answer.append(i)
    return answer