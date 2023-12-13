# 10890. 알파벳 찾기
s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = []

for i in alphabet:
    if i in s:
        result.append(s.index(i))
    else:
        result.append(-1)

for i in result:
    print(i, end = ' ')