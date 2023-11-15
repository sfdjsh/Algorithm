function solution(n) {
    var answer = 0;
    
    sqrtNum = Math.sqrt(n)
    
    return Number.isInteger(sqrtNum) ? (sqrtNum + 1) ** 2 : -1;
}