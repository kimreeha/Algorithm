

def solution(s):
    answer = []
    char = ''
    
    for i in s:
        array = []
        if i not in char:
            answer.append(-1)
        else:
            cnt = 0
            for n in char[::-1]:
                if i != n:
                    cnt += 1
                else:
                    array.append(cnt)
            array.sort()
            answer.append(array[0]+1)
        char += i

    return answer