def solution(record):
    answer = []
    
    id_nickname = {}
    for r in record:
        r = list(r.split(' '))
        if r[0] != "Leave":
            active, user_id, nickname = r[0], r[1], r[2]
            id_nickname[user_id] = nickname
    
    for r in record:
        r = list(r.split(' '))
        if r[0] == "Enter":
            answer.append(f'{id_nickname[r[1]]}님이 들어왔습니다.')
        if r[0] == "Leave":
            answer.append(f'{id_nickname[r[1]]}님이 나갔습니다.')
            
    
    return answer