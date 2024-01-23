def solution(m, musicinfos):
    answer = ['(None)', 0]
    
    m_split = ''
    for i in range(len(m) - 1):
        if m[i].isalpha():
            if m[i + 1] == '#':
                m_split += m[i] + m[i + 1]
            else:
                m_split += m[i] + '0'
    if m[-1].isalpha():
        m_split += m[-1] + '0'
    
    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        time1, time2, title, sheets = musicinfo[0].split(':'), musicinfo[1].split(':'), musicinfo[2], musicinfo[3]
        hour, minute = int(time2[0]) - int(time1[0]), int(time2[1]) - int(time1[1])
        t_gap = hour * 60 + minute
        
        sheet = []
        for i in range(len(sheets) - 1):
            if sheets[i].isalpha():
                if sheets[i + 1] == '#':
                    sheet.append(sheets[i] + sheets[i + 1])
                else:
                    sheet.append(sheets[i] + '0')
        if sheets[-1].isalpha():
            sheet.append(sheets[-1] + '0')
        
        sheet_cont = ''
        for i in range(t_gap):
            sheet_cont += sheet[i % len(sheet)]
        
        if m_split in sheet_cont and len(sheet_cont) > answer[1]:
            answer[0], answer[1] = title, len(sheet_cont)
            
    return answer[0]