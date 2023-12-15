# 11047. 동전 0

n, k = map(int, input().split())
money = [int(input()) for i in range(n)]
money.sort(reverse = True)

# 가장 높은 가치를 가진 동전부터 차례로 나눠 나간다.
# 만일 나누기 값이 0보다 작을 경우 다음 동전으로 넘어간다.

result = 0

for i in money:
    if k // i == 0:
        continue
    else:
        result += k//i
        k %= i

print(result)