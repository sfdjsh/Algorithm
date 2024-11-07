function solution(arr, divisor) {    
    arr.sort((a, b) => a - b)
    const answer = arr.filter((ele) => ele % divisor === 0)
    return answer.length? answer : [-1];
}