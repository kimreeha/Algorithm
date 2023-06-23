def solution(s):
    s = s.lower()
    p = len([i for i in s if i=='p'])
    y = len([i for i in s if i=='y'])
    if p==y:
        return True
    else:
        return False