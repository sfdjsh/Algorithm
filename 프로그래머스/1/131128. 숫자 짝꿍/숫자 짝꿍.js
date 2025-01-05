function solution(X, Y) {    
    let answer = ''
    
    function counting_num(num) {
        const num_x = X.split('').filter(val => val === num).length;
        const num_y = Y.split('').filter(val => val === num).length;
        return Math.min(num_x, num_y)
    }
    
    for (let i = 9; i >= 0; i--) {
        const min_cnt = counting_num(String(i))
        if (min_cnt > 0) {
            answer += String(i).repeat(min_cnt)
        }
    }
    
    if (answer === '') return '-1'; // 공통 숫자가 없으면 "-1"
    if (answer[0] === '0') return '0'; // 0으로만 구성된 경우 "0"
    return answer;
    
    // return answer.length >= 1 ? String(Number(answer)) : '-1'
}