# 11650. 좌표정렬하기

n = int(input())
data = [list(map(int, input().split())) for i in range(n)]

data.sort()

for i in data:
    print(*i)