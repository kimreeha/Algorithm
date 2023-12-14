# 10798. 세로읽기

s = [input() for i in range(5)]

max_len = max([len(i) for i in s])
for i in range(len(s)):
    if max_len > len(s[i]):
        s[i] += ' '* (max_len - len(s[i]))

result_lst = []
for i in range(len(s)):
    lst = [s[i][j] for j in range(len(s[0]))]
    result_lst.append(lst)
    
result = []
for i in range(len(result_lst[0])):
    lst = [result_lst[j][i] for j in range(len(result_lst))]
    result.append(lst)

char = ''
for i in result:
    char += ''.join(i)

char = char.replace(' ', '')
print(char)