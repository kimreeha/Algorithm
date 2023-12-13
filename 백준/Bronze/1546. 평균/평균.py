# 1546. 평균

n = int(input())
data = sorted(list(map(int, input().split())))

for i in range(len(data)):
    data[i] = data[i]/data[-1]*100

print(sum(data)/len(data))