function solution(x) {    
    x = String(x)
    var tmp = 0
    for (let i = 0; i < x.length; i++) {
        tmp += Number(x[i])    
    }
    
    if (Number(x) % tmp) {
        return false
    } else {
        return true
    }    
    
}