function solution(number) {
    var answer = 0;
    
    function combination(lst, idx) {
        if (lst.length === 3) {
            answer += !lst.reduce((acc, cur) => acc + cur, 0) && 1;
            return
        }
        
        for (let i = idx; i < number.length; i++) combination([...lst, number[i]], i + 1);
    }
    
    combination([], 0);
    
    return answer;
}