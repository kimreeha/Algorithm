def solution(age):
    answer = ''
    alpha = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    for i in str(age):
        if i in alpha:
            answer += alpha[i]
    return answer