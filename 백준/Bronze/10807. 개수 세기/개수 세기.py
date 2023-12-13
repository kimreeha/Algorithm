# 10807. 개수 세기

n = int(input())
data = list(map(int, input().split()))
K = int(input())

cnt = 0
for i in data:
    if K == i:
        cnt += 1

print(cnt)