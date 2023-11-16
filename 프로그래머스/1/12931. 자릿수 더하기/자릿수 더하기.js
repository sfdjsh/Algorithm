function solution(n) {
    n = String(n).split('')
    n = n.map(Number)
    
    var answer = n.reduce((a, b) => a + b, 0)
    
    return answer;
}