function solution(s, skip, index) {
    
    function changeASCII(codeAt) {
        let cnt = 0;
        while (cnt < index) {
            codeAt++;
            if (codeAt > 122) codeAt -= 26;
            if (!skip.includes(codeAt)) cnt++;
        }
        
        return codeAt;
    }
    
    var answer = '';
        
    skip = skip.split('').map(char => char.charCodeAt());
    for (let char of s) {
        let codeAt = char.charCodeAt();
        answer += String.fromCharCode(changeASCII(codeAt));
    }  
    
    return answer;
}