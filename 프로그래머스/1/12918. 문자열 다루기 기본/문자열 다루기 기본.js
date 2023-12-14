function solution(s) {
    var answer = false;
        
    if (s.length === 4 || s.length === 6) {
        answer = (s == parseInt(s)) ? true : false
    }
    
    return answer
}