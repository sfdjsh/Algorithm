function solution(n, m) {
    let gcd = 1;    // 최대공약수
    while (n > 1 && m > 1) {
        let flag = false;
        for (let i = 2; i <= Math.min(n, m); i++) {
            if (n % i == 0 && m % i == 0) {
                gcd *= i;
                n /= i;
                m /= i;
                flag = true;
                break
            }
        }
        if (flag == false) break; 
    }
        
    return [gcd, gcd * n* m];
}