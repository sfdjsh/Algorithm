function solution(k, score) {
    var answer = [];
    
    let honorList = [];
    for (let num of score) {
        if (honorList.length < k) honorList.push(num);
        else {
            if (num >= honorList[0]) {
                honorList.shift();
                honorList.push(num);
            }
        }
        honorList.sort((a, b) => a - b);
        answer.push(honorList[0]);
    }
    
    return answer;
}