function solution(id_list, report, k) {
    var answer = [];
    var report_list = {};
    
    id_list.map(id => {
        report_list[id] = [];
        answer.push(0);
    })
    
    // 신고당한 사람을 key, 신고한 사람을 value로 report_list에 넣어주기
    report.map((user) => {
        const [reporting_id, reported_id] = user.split(' ');
        if (!report_list[reported_id].includes(reporting_id)) report_list[reported_id].push(reporting_id);
    })
    
    for (let key in report_list) {
        if (report_list[key].length >= k) {     // report_list에서 신고당한 사람(key)의 신고 횟수가 k회 이상일 때
            report_list[key].map((user) => {
                // 신고한 유저에게 메일 발송(count 증가) 
                const idx = id_list.indexOf(user);
                answer[idx]++;
            })
        }
    }

    return answer;
}