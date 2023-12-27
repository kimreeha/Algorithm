def solution(s):
    s = list(s.split(' '))
    word_lst = []
    
    for i in s:
        word = ''
        if i == '':
            word += i
            word_lst.append(word)
        else:
            word += i[0].upper()
            word += i[1:].lower()
            word_lst.append(word)
            
    return ' '.join(word_lst)