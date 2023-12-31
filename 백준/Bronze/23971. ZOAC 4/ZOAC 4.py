H, W, N, M = map(int, input().split())

x, y = 0, 0

x_cnt, y_cnt = 0, 0
for i in range(H):
    if y < H:
        y += N+1
        y_cnt += 1

for i in range(W):
    if x < W:
        x += M+1
        x_cnt += 1
    
print(x_cnt*y_cnt)