def solution(n):
    answer = 0
    jari = []
    
    while n > 0:
        jari.append(n%3)
        n //= 3

    jari = jari[::-1]
    
    for i in range(len(jari)):
        answer += jari[i]*(3**i)
        
    return answer