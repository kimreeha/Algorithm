def solution(x):
    total = sum(map(int, [i for i in str(x)]))
    if x%total==0:
        return True
    else:
        return False