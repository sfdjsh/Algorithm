function solution(n, m) {
    var answer = [];
    
    let maxN = 1;
    let minN = 1;
    while (n > 1 && m > 1) {
        let flag = false;
        for (let i = 2; i <= Math.min(n, m); i++) {
            if (n % i == 0 && m % i == 0) {
                maxN *= i;
                n /= i;
                m /= i;
                flag = true;
                break
            }
        }
        if (flag == false) { break }
    }
    
    minN = maxN * n * m 
    
    return [maxN, minN];
}