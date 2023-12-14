# 2745. 진법 변환

n, b = input().split()
b = int(b)

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nums = list(range(10,36))

n = [int(i) if i not in alpha else i for i in n][::-1]

result = 0
for i in range(len(n)):
    if n[i] in alpha:
        result += nums[alpha.index(n[i])]*b**i
    else:
        result += n[i]*b**i
print(result)