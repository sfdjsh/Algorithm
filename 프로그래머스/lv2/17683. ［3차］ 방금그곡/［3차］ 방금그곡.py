def solution(m, musicinfos):
    answer = ''  
    max_time = 0    # 가장 긴 음악을 시간을 체크하기 위해 만든 변수
    
    # 악보에 #이 들어간 경우 소문자로 변환 ex) C# -> c
    changed_m = ''
    for i in range(len(m)):
        if m[i] == '#':
            continue
        if i < len(m) - 1 and m[i+1] == '#':
            changed_m += m[i].lower()
        else:
            changed_m += m[i]
    
    
    for music in musicinfos:
        info_list = []                                  # 악보 정보를 담을 리스트
        start, end, title, info = music.split(',')      # 시작 시각, 끝난 시각, 음악 제목, 악보 정보
        
        # 악보에 #이 들어간 경우 소문자로 변환
        for i in range(len(info)):
            if info[i] == '#':
                continue
            if i < len(info) - 1 and info[i+1] == '#':
                info_list.append(info[i].lower())
            else:
                info_list.append(info[i])
        
        s_h, s_m = start.split(':')         # 시작 시각의 시, 분으로 나누기
        e_h, e_m = end.split(':')           # 끝난 시각의 시, 분으로 나누기
        
        time_gap = (int(e_h) - int(s_h)) * 60 + (int(e_m) - int(s_m))   # 음악이 재생된 시간
        
        # 음악이 재생된 시간만큼 반복문을 돌아, 악보 정보 리스트의 인덱스로 melody 이어가기
        melody = ''
        for i in range(time_gap):
            melody += info_list[i % len(info_list)]
        
        if changed_m in melody:         # 네오가 기억한 멜로디와 방송된 곡의 정보가 같을 때
            if max_time < time_gap:     
                max_time = time_gap     # 재생된 시간의 제일 긴 음악 시간 갱신
                answer = title          # 음악 제목 반환
    
    # 조건이 일치하는 음악이 없을 때, None 반환
    if not answer:
        answer = '(None)'
                    
    return answer