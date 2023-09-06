def solution(players, callings):
    dict = {players[i] : i for i in range(len(players))}
    for c in callings:  
        idx = dict[c]
        dict[c] -= 1
        dict[players[idx - 1]] += 1
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
    
    return players