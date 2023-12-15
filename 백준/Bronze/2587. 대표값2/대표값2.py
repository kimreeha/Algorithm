# 2587. 대표값2

n = 5
data = [int(input()) for i in range(n)]
data.sort()

# 평균 출력
print(int(sum(data)/len(data)))

if len(data)%2 != 0:
    print(int(data[len(data)//2]))
else:
    print(int((data[len(data)//2-1] + data[len(data)//2+1])/2))