function solution(arr) {
    let min_num = Math.min(...arr)
    let answer = arr.filter(e => e !== min_num)
        
    return (answer.length === 0) ? [-1] : answer
}