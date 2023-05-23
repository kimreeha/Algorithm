n = int(input())
lst = []
answer = ''
for i in range(1, n+1):
    lst.append('*'*i)
for v in lst:
    answer += v+ '\n'
print(answer)
    