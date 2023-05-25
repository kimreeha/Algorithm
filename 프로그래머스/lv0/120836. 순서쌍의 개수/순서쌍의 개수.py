def solution(n):
    order_twin = []
    for i in range(1, n+1):
        if n % i == 0:
            order_twin.append([i, n // i])
    answer = len(order_twin)
    return answer