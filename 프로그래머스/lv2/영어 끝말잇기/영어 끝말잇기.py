# 1. 번호와 차례를 반환할 변수를 정의한다.
# 2. 단어를 하나씩 받을 리스트를 정의한다.
# 3. words를 순회하며 리스트의 단어 끝과 words의 첫 단어를 비교한다.
# 4. 혹은 words의 요소가 리스트 안에 이미 있는지 확인한다.

def solution(n, words):
    answer = []
    lst = [words[0]]
    num, repeat = 1, 1
    
    for word in words[1:]:
        num += 1
        if lst[-1][-1] != word[0] or word in lst:
            answer.append(num)
            answer.append(repeat)
            break
        else:
            lst.append(word)
            
        if num%n == 0:
            num = 0
            repeat += 1
            
    if len(answer) == 0:
        return [0,0]
    else:
        return answer 