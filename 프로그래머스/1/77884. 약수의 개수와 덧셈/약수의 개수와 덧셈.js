function solution(left, right) {
    var answer = 0;
    
    function prime_check(num) {
        let cnt = 0;
        for (let i = 1; i <= parseInt(num ** (1/2)); i++) {
            if (num % i === 0) i * i === num? cnt += 1 : cnt += 2;
        }        
        return cnt % 2 ? false : true;
    }
    
    for (let i = left; i <= right; i++) {
        prime_check(i)? answer += i : answer -= i;
    }
    
    return answer;
}