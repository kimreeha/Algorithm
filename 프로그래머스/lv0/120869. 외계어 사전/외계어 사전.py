def solution(spell, dic):
    dic_ = [''.join(sorted(i)) for i in dic]
    if ''.join(sorted(spell)) in dic_:
        return 1
    else:
        return 2