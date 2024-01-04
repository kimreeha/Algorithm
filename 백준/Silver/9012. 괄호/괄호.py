T = int(input())

for i in range(T):
    s = input()
    while len(s) > 0:
        if '()' in s:
            s = s.replace('()','')
        else:
            break

    if len(s) != 0:
        print('NO')
    else:
        print('YES')