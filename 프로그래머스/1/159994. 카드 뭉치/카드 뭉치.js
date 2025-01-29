function solution(cards1, cards2, goal) {
    
    for (let char of goal) {
        if (char === cards1[0]) cards1.shift();
        else if (char === cards2[0]) cards2.shift();
        else return "No";
    }
    
    return "Yes";
}