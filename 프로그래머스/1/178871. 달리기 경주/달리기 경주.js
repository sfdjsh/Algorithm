function solution(players, callings) {
    var answer = [...players];
    
    const playerList = {}
    for (let i = 0; i < answer.length; i++) {
        playerList[answer[i]] = i;
    }
    
    for (let calling of callings) {
        const index = playerList[calling];
        playerList[calling]--;
        playerList[answer[index - 1]]++;
        
        const tmp = answer[index - 1];
        answer[index - 1] = calling;
        answer[index] = tmp;
    }
    
    return answer;
}