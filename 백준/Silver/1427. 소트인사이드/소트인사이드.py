# 1427. 소트인사이드

n = int(input())
data = [int(i) for i in str(n)]
data.sort(reverse= True)

char = ''
for i in data:
    char += str(i)
print(char)