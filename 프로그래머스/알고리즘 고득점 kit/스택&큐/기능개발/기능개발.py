# 1. 작업 진도(progresses)를 앞 기능부터 받는 큐를 생성한다.
# 2. 큐에 들어온 작업진도를 speeds의 작업속도만큼 더한다.
# 3. day 변수를 생성하여 하루가 지날때 마다 1씩 더한다.
# 4. 작업 진도가 100을 넘어가는 요소를 앞에서부터 큐에서 빼낸다.
# 5. 같은 날 큐에서 빠진 요소의 수를 세고 그 수를 answer 리스트에 추가한다.
# 6. 이 과정을 큐의 모든 원소가 없어질 때 까지 반복한다.

def solution(progresses, speeds):
    answer = []  # 결과를 담을 리스트
    day = 0  # 경과 일수
    cnt = 0 
    queue = list(progresses[::-1])  
    
    while queue:  # 큐가 빌 때까지 반복
        # 각 작업 진도에 작업 속도를 더함
        for i in range(len(queue)):
            queue[i] += speeds[::-1][i]
        
        day += 1  # 하루가 지남

        while queue and queue[-1] >= 100:
            queue.pop()
            cnt += 1
        
        # 하루에 배포된 작업 수를 결과 리스트에 추가하고 초기화
        if cnt > 0:
            answer.append(cnt)
            cnt = 0
    
    return answer
