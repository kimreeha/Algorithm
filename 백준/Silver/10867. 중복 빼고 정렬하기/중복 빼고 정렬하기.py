# 10867. 중복 빼고 정렬하기

T = int(input())
N = list(map(int, input().split()))
N = sorted(list(set(N)))

print(*N)