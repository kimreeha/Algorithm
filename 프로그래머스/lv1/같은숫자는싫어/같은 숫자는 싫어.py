def solution(arr):
    answer = [arr[0]]
    stack = [arr[0]]
    
    for i in range(1,len(arr)):
        if stack[-1] == arr[i]:
            stack.append(arr[i])
        else:
            stack.append(arr[i])
            answer.append(arr[i])
            

    return answer