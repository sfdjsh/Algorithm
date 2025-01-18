function solution(s) {
    var answer = 0;
    s = s.split('');
        
    while (true) {
        const firstString = s[0];
        
        let cnt1 = 0, cnt2 = 0;
        for (let i = 0; i < s.length; i++) {
            if (s[i] === firstString) cnt1++;
            else cnt2++;     
            if (cnt1 === cnt2) {
                s = s.slice(i + 1, s.length);
                answer++;
                break;
            }
        }
        
        if (s.length === 0) break;
        
        if (cnt1 !== cnt2) {
            answer++;
            break;
        }        
    }    
    
    return answer;
}