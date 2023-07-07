def solution(a, b):
    c = [i for i in range(1,a+1) for j in range(1, b+1) if (a%i==0)&(b%j==0)&(i==j)][-1]
    b //= c
    answer= []
    d = 2
    while d <= b: 
        if b % d == 0: 
            answer.append(d)
            b = b / d 
        else: 
            d = d + 1
    result = [True if (i==2)|(i==5) else False for i in list(set(answer))]
    if False in result:
        return 2
    else:
        return 1