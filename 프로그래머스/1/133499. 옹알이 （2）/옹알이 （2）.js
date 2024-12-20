function solution(babbling) {
    var answer = 0;
    const possible_speak = ['aya', 'ye', 'woo', 'ma'];
    for (let bab of babbling) {
        let speaking = '', speaked = '';    // speaking = 말하고 있는 단어, speaked = 말했던 발음
        for (let speak of bab) {
            speaking += speak;
            if (possible_speak.includes(speaking) && speaking !== speaked) {
                speaked = speaking;
                speaking = '';
            }
        }
        
        if (!speaking) answer++;
    }
        
    return answer;
}