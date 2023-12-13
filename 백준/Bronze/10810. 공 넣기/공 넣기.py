### 10810. 공 넣기

n, m = map(int, input().split())

ball_nums = [0]*n

for _ in range(m):
    i, j, k = map(int, input().split())
    ball_nums[i-1:j] = [k for v in range(i-1, j)]

for i in ball_nums:
    print(i, end = ' ')   