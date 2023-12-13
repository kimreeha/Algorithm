# 3003. 킹, 퀸, 룩, 비숍, 나이트, 폰

data = list(map(int, input().split()))
pieces = [1, 1, 2, 2, 2, 8]
needs = [0]*6

for i in range(len(data)):
    needs[i] = pieces[i]-data[i]

for i in needs:
    print(i, end = ' ')