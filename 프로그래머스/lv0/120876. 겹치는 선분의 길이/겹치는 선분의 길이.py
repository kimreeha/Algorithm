def solution(lines):
    a = [i for i in range(lines[0][0],lines[0][1])]
    b = [i for i in range(lines[1][0],lines[1][1])]
    c = [i for i in range(lines[2][0],lines[2][1])]
    return len(list(set([i for i in b if i in c] + [i for i in a if i in b] + [i for i in a if i in c])))