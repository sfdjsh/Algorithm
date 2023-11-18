function solution(s, n) {
    var answer = '';
    
    let upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    let lower = 'abcdefghijklmnopqrstuvwxyz'
        
    for (let i = 0; i < s.length; i++) {
        if (s[i] === ' ') {
            answer += ' ';
        } else {
            const upLow = upper.includes(s[i]) ? upper : lower;
            let idx = upLow.indexOf(s[i]) + n;
            if (idx >= upLow.length) {
                idx -= upLow.length;
            }
            
            answer += upLow[idx];            
        }
    }
    
    return answer;
}