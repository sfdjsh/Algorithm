def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    dic = {}
    for i in id_list:
        dic[i] = 0
        
    report = set(report)    # 동일한 유저 신고 중복 제거                    
    for r in report:
        use_id, report_id = r.split(' ')    # 신고자 id, 신고 당한 id
        dic[report_id] += 1
    
    for r in report:
        use_id, report_id = r.split(' ')
        if dic[report_id] >= k:     # 신고 당한 id가 신고 횟수 이상일 때
            answer[id_list.index(use_id)] += 1  # 신고한 id가 받는 메일 수 추가
    
    return answer