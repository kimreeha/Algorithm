# 2292. 벌집
import math
N = int(input())

x, i = 1, 1
result = 1

while x < N:
    result += 1
    x += 6*i
    i += 1
    
print(result)