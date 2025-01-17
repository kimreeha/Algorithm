def solution(s):
    stack = []
    for x in s:
        stack.append(x)
        if stack[-2::] == ['(', ')']:
            stack.pop()
            stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False