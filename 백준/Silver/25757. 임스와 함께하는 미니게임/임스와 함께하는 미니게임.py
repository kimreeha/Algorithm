# 25757. 임스와 함께하는 미니게임

N, game = input().split()
N = int(N)
array = []

for _ in range(N):
    array.append(input())

array = set(array)

if game == 'Y':
    print(len(array)//1)
elif game == 'F':
    print(len(array)//2)
else:
    print(len(array)//3)