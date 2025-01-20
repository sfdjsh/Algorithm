function solution(s) {
    var answer = [];
    
    let strMap = new Map();
    for (let i = 0; i < s.length; i++) {
        if (strMap.get(s[i]) === undefined) {
            answer.push(-1);
            strMap.set(s[i], i);
        } else {
            answer.push(i - strMap.get(s[i]));
            strMap.set(s[i], i);
        }
    }
    
    return answer;
}