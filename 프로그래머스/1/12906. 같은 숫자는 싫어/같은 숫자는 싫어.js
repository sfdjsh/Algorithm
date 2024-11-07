function solution(arr) {
    var answer = [];
    var tmp = 10;
    
    for (element of arr) {
        if (tmp !== element) {
            answer.push(element);
            tmp = element;
        }
    }
    
    return answer;
}