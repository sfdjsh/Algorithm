function solution(lottos, win_nums) {
    const lotto_rank = { 6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}
        
    let max_cnt = 0, min_cnt = 0;
    for (let num of win_nums) {
        if (lottos.includes(num)) {
            max_cnt++;
            min_cnt++;
        }
    }
    max_cnt += lottos.filter(e => !e).length;    // 알아볼 수 없는 번호(0)를 최고 순위에 더하기       
    
    return [lotto_rank[max_cnt], lotto_rank[min_cnt]];
}