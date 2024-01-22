# 7568. 덩치

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
ranks = []

for xy in array:
    cnt = 1
    for pq in array:
        if xy[0] == pq[0] and xy[1] == pq[1]:
            continue
        if xy[0] < pq[0] and xy[1] < pq[1]:
            cnt += 1
    ranks.append(cnt)
print(*ranks)