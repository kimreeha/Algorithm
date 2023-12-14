# 1436. 영화감독 숌

n = int(input())

cnt, num = 0, 0

while True:
    num += 1
    if '666' in str(num):
        cnt +=1
    if cnt == n:
        break

print(num)