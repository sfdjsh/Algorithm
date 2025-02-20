function solution(friends, gifts) {
    const len = friends.length;
    const answer = Array(len).fill(0);
    const giveGift = Array.from({length : len}, () => Array(len).fill(0));
    const giftScore = Object.fromEntries(friends.map(name => [name, 0]));
    
    gifts.map(gift => {
        const [give, take] = gift.split(' ');
        giveGift[friends.indexOf(give)][friends.indexOf(take)]++;
        giftScore[give]++;
        giftScore[take]--;
    })
    
    for (let i = 0; i < len; i++) {
        for (let j = i + 1; j < len; j++) {
            if (giveGift[i][j] < giveGift[j][i]) answer[j]++;
            else if (giveGift[j][i] < giveGift[i][j]) answer[i]++;
            else {
                if (giftScore[friends[i]] > giftScore[friends[j]]) answer[i]++;
                else if (giftScore[friends[i]] < giftScore[friends[j]]) answer[j]++;
            }
        }
    }
        
    return Math.max(...answer)
}