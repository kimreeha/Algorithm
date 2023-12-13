# 2530. 인공지능 시계

hour, minute, second = map(int, input().split())
wait = int(input())

tot_sec = hour*3600 + minute*60 + second + wait
array = [3600, 60, 1]
result = []

for i in array:
    result.append(tot_sec//i)
    tot_sec %= i

if result[0] >= 24:
    result[0] = result[0]%24
elif result[1] >= 60:
    result[1] = result[1]%60
    result[0] += result[1]//60

for i in result:
    print(i, end =' ')