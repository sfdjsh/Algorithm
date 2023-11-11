function solution(arr) {
    var answer = 0;
    
    let sum = 0
    
    arr.forEach(num => {
        sum += num
    })
    
    return sum / arr.length;
}