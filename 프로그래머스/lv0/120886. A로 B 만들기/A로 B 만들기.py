def solution(before, after):
    b = sorted([i for i in before])
    a = sorted([i for i in after])
    if a == b:
        return 1
    else:
        return 0