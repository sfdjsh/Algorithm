function solution(number, limit, power) {
    var answer = 0;
    
    function buying_weapon(num) {
        if (num === 1) {
            answer++;
            return
        }
        
        let count = 0;
        for (let i = 1; i <= num**(1/2); i++) {
            if (num % i === 0) {
                if (i * i === num) count++;
                else count += 2;
            }
        }
        
        answer += count <= limit ? count : power;
        return
    }
    
    for (let num = 1; num <= number; num++) buying_weapon(num)
    
    return answer;
}