# 5585. 거스름돈
array = [500, 100, 50, 10, 5, 1]
n = 1000 - int(input())

result = 0

for x in array:
    cnt = n//x
    n -= x * cnt
    result += cnt
    
print(result)