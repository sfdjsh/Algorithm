function solution(new_id) {
    var answer = '';
    
    // 1단계
    new_id = new_id.toLowerCase();
    
    // 2단계
    const pos_str = /[a-zA-Z0-9\-_\.]/;
    for (let str of new_id) {
        if (pos_str.test(str)) answer += str;
    }
    
    // 3단계
    let idx = 0
    while (idx < answer.length - 1) {
        if (answer[idx] === '.' && answer[idx + 1] === '.') answer = answer.slice(0, idx) + answer.slice(idx + 1);
        else idx ++;
    }
    
    // 4단계
    if (answer[0] === '.') answer = answer.slice(1);
    if (answer[answer.length - 1] === '.') answer = answer.slice(0, answer.length - 1);
    
    // 5단계
    if (!answer) answer += 'a';
    
    // 6단계
    if (answer.length >= 16) {
        answer = answer.slice(0, 15);
        if (answer[answer.length - 1] === '.') answer = answer.slice(0, answer.length - 1);
    }
    
    // 7단계
    while (answer.length <= 2) answer += answer[answer.length - 1];
  
    return answer;
}