function solution(n) {
    
    var arr = []
    
    n = String(n).split('');
    n = n.map(Number);
    for (let i = n.length - 1; i >= 0; i--) {
        arr.push(n[i])
    }
    
    return arr;
}