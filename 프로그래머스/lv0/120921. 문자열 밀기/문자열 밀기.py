def solution(A, B):
    new_A = [A[i::]+A[:i] for i in range(len(A),0,-1)]
    if B in new_A:
        return new_A.index(B)
    else:
        return -1