# 2720. 세탁소 사장 동혁

t = int(input())

for _ in range(t):
    n = int(input())

    money = [25, 10, 5, 1]
    lst = []
    
    for i in money:
        lst.append(n//i)
        n %= i
        
    for i in lst:
        print(i, end = ' ')