def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append(numbers[-1])
        answer.extend([i for i in numbers])
        answer.pop()
    else:
        answer.append(numbers[1])
        answer.extend([numbers[i] for i in range(2, len(numbers))])
        answer.append(numbers[0])
    return answer