# 2738. 행렬덧셈

n, m = map(int, input().split())
mat1 = [list(map(int, input().split())) for i in range(n)]
mat2 = [list(map(int, input().split())) for i in range(n)]

result = []

for i in range(n):
    lst = []
    for j in range(m):
        lst.append(mat1[i][j] + mat2[i][j])
    result.append(lst)

for i in range(n):
    char = ''
    for j in range(m):
        char += str(result[i][j]) + ' '
    print(char)