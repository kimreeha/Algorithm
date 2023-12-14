# 2566. 최댓값

data = [list(map(int, input().split())) for i in range(9)]

max_grp = [max(i) for i in data]

max_num = max(max_grp)

print(max_num)
for i in range(9):
    for j in range(9):
        if data[i][j] == max_num:
            print(i+1, j+1)