function solution(answers) {
    var answer = []
    var correct_cnt = [0, 0, 0];
    
    var soopo1 = [1, 2, 3, 4, 5]
    var soopo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    var soopo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    var answer_key1 = []
    var answer_key2 = []
    var answer_key3 = []
    for (let i = 0; i < answers.length; i += soopo1.length) {
        answer_key1.push(...soopo1)
        answer_key2.push(...soopo2)
        answer_key3.push(...soopo3)
    }
    
    for (let i = 0; i < answers.length; i++) {
        if (answer_key1[i] === answers[i]) correct_cnt[0]++
        if (answer_key2[i] === answers[i]) correct_cnt[1]++
        if (answer_key3[i] === answers[i]) correct_cnt[2]++
    }
    
    max_cnt = Math.max(...correct_cnt)
    for (let i = 0; i < correct_cnt.length; i++) {
        if (correct_cnt[i] === max_cnt) answer.push(i + 1)
    }
    
    return answer;
}