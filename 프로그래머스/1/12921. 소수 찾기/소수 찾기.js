function solution(n) {
    var answer = 0;
    
    const arr = []
    for (let i = 2; i <= n; i++) {
        arr[i] = i
    }
    
    for (let i = 2; i <= n; i++) {
        if (arr[i] === 0) continue;
        for (let j = i * 2; j <= n; j += i) {
            arr[j] = 0
        }
    }
    
    return arr.filter(e => e !== 0).length;
}