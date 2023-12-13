# 2525. 오븐 시계

hour, minute = map(int, input().split())
wait = int(input())

tot_min = hour*60 + minute + wait

if tot_min//60 >= 24:
    print(tot_min//60-24, tot_min%60)
else:
    print(tot_min//60, tot_min%60)