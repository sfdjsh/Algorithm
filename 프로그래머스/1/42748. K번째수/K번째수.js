function solution(array, commands) {
    var answer = [];
    
    commands.map(num => {
        const slice_lst = array.slice(num[0] - 1, num[1]);
        slice_lst.sort((a, b) => a - b);
        answer.push(slice_lst[num[2] - 1]);
    })
    
    return answer;
}