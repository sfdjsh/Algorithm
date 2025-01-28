function solution(today, terms, privacies) {
    var answer = [];
    
    const [tdYear, tdMonth, tdDay] = today.split('.').map(Number);
    const tdCnt = tdYear * 336 + tdMonth * 28 + tdDay;
    
    const termDict = {}; 
    for (let term of terms) {
        const [type, cnt] = term.split(' ');
        termDict[type] = cnt;
    }
    
    for (let i = 0; i < privacies.length; i++) {
        const [date, type] = privacies[i].split(' ');
        let [year, month, day] = date.split('.').map(Number);
        month += Number(termDict[type]);
        const cnt = Number(year) * 336 + Number(month) * 28 + day;
        
        if (cnt <= tdCnt) answer.push(i + 1);
    }   
    
    return answer;
}