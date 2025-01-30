function solution(keymap, targets) {
    var answer = [];
    
    const dict = {};
    for (let key of keymap) {
        for (let i = 0; i < key.length; i++) {
            if (key[i] in dict) {
                if (dict[key[i]] >= i + 1) dict[key[i]] = i + 1;
            } 
            else dict[key[i]] = i + 1;
        }
    }
    
    for (let target of targets) {
        let cnt = 0;
        for (let tg of target) {
            if (tg in dict) cnt += dict[tg] ;
            else {
                cnt = -1;
                break;
            }
        }
        answer.push(cnt);
    }
    
    return answer;
}