def solution(players, callings):
    # 순위 담는 딕셔너리 생성
    dict_ = {player : rank for rank, player in enumerate(players)}
    
    for x in callings:
        # 현재 순위
        order = dict_.get(x)
        
        if order > 0:
            pre_player = players[order - 1]
            players[order-1], players[order] = x, pre_player
            
            dict_[pre_player] += 1
            dict_[x] -= 1
    
    return players