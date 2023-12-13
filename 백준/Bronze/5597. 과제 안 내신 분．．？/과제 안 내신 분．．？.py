# 5597. 과제 안내신 분..?

data = set([int(input()) for i in range(28)])
id = set([i for i in range(1,31)])

data = list(id - data)
data.sort()

for i in data:
    print(i)