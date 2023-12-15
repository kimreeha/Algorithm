### 2750. 수 정렬하기
# 시간 복잡도가 (O2)인 알고리즘으로 풀이

n= int(input())
lst = [int(input()) for i in range(n)]
lst.sort()

for i in lst:
    print(i)