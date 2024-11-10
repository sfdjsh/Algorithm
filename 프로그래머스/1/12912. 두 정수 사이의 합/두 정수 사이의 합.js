function solution(a, b) {
    var answer = 0;
    const min_num = Math.min(a, b), max_num = Math.max(a, b); 
    for (let i = min_num; i <= max_num; i++) answer += i;
    return answer;
}