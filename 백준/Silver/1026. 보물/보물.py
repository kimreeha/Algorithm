## 1026. 보물

# 1. B의 최대값 인덱스를 찾는다.
# 2. A의 최솟값을 B의 최댓값 인덱스에 맞게 재배열한다.
# 3. 두 수를 곱한다.
# 3. B의 최댓값과 A의 최솟값을 삭제한다.
# 4. 모든 과정을 반복한다.

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0

while len(A) > 0:
    A[A.index(min(A))], A[B.index(max(B))] = A[B.index(max(B))], A[A.index(min(A))]
    result += A[B.index(max(B))]*B[B.index(max(B))]
    A.remove(min(A))
    B.remove(max(B))

print(result)