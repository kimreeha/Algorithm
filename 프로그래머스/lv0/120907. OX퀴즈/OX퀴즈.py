def solution(quiz):
    answer = [[eval(i[:i.find('=')]), int(i.split(' ')[-1])] for i in quiz]
    return ['O' if len(set(i)) == 1 else 'X' for i in answer]