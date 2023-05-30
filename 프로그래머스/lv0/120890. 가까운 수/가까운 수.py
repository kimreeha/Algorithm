def solution(array, n):
    min_num = min([abs(n-i) for i in array])
    return sorted([i for i in array if min_num == abs(n-i)])[0]