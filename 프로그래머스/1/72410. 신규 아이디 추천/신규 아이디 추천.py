def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()     # 1단계
    new_id = list(new_id)
    
    # 2단계
    uniq = []
    for up_id in new_id:
        if not up_id.isalpha() and not up_id.isdigit() and up_id not in ['-', '_', '.']:
            uniq.append(up_id)            
    
    for u in uniq:
        new_id.remove(u)
    
    # 3단계
    if new_id:
        idx = 0
        while idx < len(new_id) - 1:
            if new_id[idx] == '.' and new_id[idx + 1] == '.':
                del new_id[idx]
            else:
                idx += 1
    
    # 4단계
    while new_id:
        if new_id[0] == '.':
            del new_id[0]            
        elif new_id[-1] == '.':
            del new_id[-1]
        else:
            break
    
    # 5단계
    if not new_id:
        new_id.append('a')
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    if new_id[-1] == '.':
        del new_id[-1]
    
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id.append(new_id[-1])
            
    new_id = ''.join(new_id)
    
    return new_id