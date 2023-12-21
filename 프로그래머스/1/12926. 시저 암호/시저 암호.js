function solution(s, n) {
    var answer = '';
    
    for (let i = 0; i < s.length; i ++) {
        let e_idx = s[i].charCodeAt();
        if (e_idx >= 65 && e_idx <= 90) {
            e_idx += n;
            if (e_idx > 90) {
                e_idx -= 26;
            }
        } else if (e_idx >= 97 && e_idx <= 122) {
            e_idx += n;
            if (e_idx > 122) {
                e_idx -= 26;
            }
        }

        answer += String.fromCharCode(e_idx);
        
    }
    
    return answer;
}