function solution(k, m, score) {
    var answer = 0;
    
    score.sort((a, b) => b - a);
    for (let i = 0; i < score.length; i += m) {
        const score_slice = score.slice(i, i + m);
        if (score_slice.length === m) answer += Math.min(...score_slice) * m;
    }
    
    return answer;
}