function solution(s, skip, index) {
    
    function changeIdx(codeAt) {
        let idx = 0;
        while (idx < index) {
            codeAt++
            if (!skip.includes(codeAt)) {
                idx++
            }
        }
        if (codeAt > 122) {
            return codeAt - 26
        }
        return codeAt
    }
    
    var answer = '';
    
    skip = skip.split('').map(char => char.charCodeAt());
    
    for (let char of s) {
        let codeAt = char.charCodeAt()
        answer += String.fromCharCode(changeIdx(codeAt))
    }  
    
    return answer;
}