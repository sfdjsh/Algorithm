function solution(n, m, section) {
    var answer = 1;
    
    let paint = section[0];
    for (let i = 1; i < section.length; i++) {
        if (section[i] - paint >= m) {
            answer++;
            paint = section[i];
        }
    }
    
    return answer;
}