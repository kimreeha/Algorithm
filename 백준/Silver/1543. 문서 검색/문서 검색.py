# 1543. 문서 검색

s = input()
char = input()

cnt = ''
result = 0

for x in s:
    cnt += x
    if char in cnt:
        result += 1
        cnt = ''

print(result)