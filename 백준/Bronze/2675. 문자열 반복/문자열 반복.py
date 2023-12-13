##### 2675. 문자열 반복
t = int(input())

for _ in range(t):
    r, s = input().split()
    ans = ''
    r = int(r)
    for v in s:
        for i in range(r):
            ans += v
    print(ans)
