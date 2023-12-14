# 2798. 블랙잭(Brute Force)

from itertools import permutations

n, m = map(int, input().split())
data = list(map(int, input().split()))

lst = list(permutations(data, 3))

hap = max([sum(i) for i in lst if sum(i) <= m])
print(hap)