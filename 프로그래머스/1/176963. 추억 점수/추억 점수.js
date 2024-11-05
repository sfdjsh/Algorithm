function solution(name, yearning, photo) {
    var answer = [];
    
    const scoreMap = new Map();
    
    for (let i = 0; i < name.length; i++) {
        scoreMap.set(name[i], yearning[i])
    }
    
    for (photo_name of photo) {
        var sum_score = 0
        for (n of photo_name) {
            if (scoreMap.get(n)) {
                sum_score += scoreMap.get(n)
            }
        }
        answer.push(sum_score)
    }    
    
    
    return answer;
}