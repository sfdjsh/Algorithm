function solution(n) {
    var answer = 0;
        
    for (let i = 0; i < parseInt(Math.sqrt(n)) + 1; i++) {
        if (n % i == 0) {
            answer += i;
            if (i * i !== n) {
                answer += n / i;
            }
        }
    }
        
    return answer;
}