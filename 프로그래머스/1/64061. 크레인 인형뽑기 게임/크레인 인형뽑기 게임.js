function solution(board, moves) {
    var answer = 0;
    let basket = [];
    
    for (let move of moves) {
        for (let i = 0; i < board.length; i++) {
            if (board[i][move - 1]) {
                basket.push(board[i][move - 1]);
                board[i][move - 1] = 0;
                break;
            }           
        }
        
        if (basket.length >= 2 && (basket[basket.length - 1] === basket[basket.length - 2])) {
            answer += 2;
            basket.splice(basket.length - 2, 2);
        }
    }
        
    return answer;
}