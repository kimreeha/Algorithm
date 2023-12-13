# 5622. 다이얼

s = input()
alp = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS','TUV', 'WXYZ']
score = [3,4,5,6,7,8,9,10]

result = 0
for i in s:
    for j in range(len(alp)):
        if i in alp[j]:
            result += score[j]
print(result)