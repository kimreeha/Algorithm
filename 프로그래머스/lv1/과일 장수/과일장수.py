def solution(k, m, score):
    # 1. 사과를 내림차순으로 정렬하여 m개씩 리스트에 원소로 담는다
    # 2. 만일 사과의 리스트가 m의 배수가 아니라면 그 나머지를 제거한다
    # 3. 한 상자의 최솟값 x 리스트 길이를 모두 더한 answer를 반환한다
    score.sort(reverse = True)
    answer = 0
    
    if len(score)%m != 0:
        score = score[:len(score)-len(score)%m]
        
    boxes, box = [], []
    
    for i in score:
        if len(box) < m:
            box.append(i)
        if len(box) == m:
            boxes.append(box)
            box = []

    for i in boxes:
        answer += min(i)*len(i)
    return answer