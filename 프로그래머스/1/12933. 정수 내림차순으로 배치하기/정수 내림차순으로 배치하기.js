function solution(n) {    
    n = String(n);
    lstN = [ ...n ];
    
    lstN = lstN.sort((a, b) => {
        return b - a
    })
    
    var answer = Number(lstN.join(''))
    
    return answer;
}