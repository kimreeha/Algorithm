# 25304. 영수증

total = int(input())
n = int(input())

result = 0
for i in range(n):
    pri, nums = map(int, input().split())
    result += pri*nums
    
if result == total:
    print('Yes')
else:
    print('No')