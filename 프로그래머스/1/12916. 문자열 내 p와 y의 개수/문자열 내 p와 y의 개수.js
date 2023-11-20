function solution(s){
    var answer = true;
    
    let cntP = 0, cntY = 0;
    s.split('').map(data => {
        if (['p', 'P'].includes(data) ) {
            cntP += 1;
        } else if (['y', 'Y'].includes(data)) {
            cntY += 1;
        }
    })
    
    return cntP === cntY ? true : false;
}