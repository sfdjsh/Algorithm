function solution(arr1, arr2) {
    var answer = [[]];
    
    let lenX = arr1.length;
    let lenY = arr1[0].length;
    
    for (let i = 0; i < lenX; i++) {
        answer[i] = [];
        for (let j = 0; j < lenY; j++) answer[i].push(arr1[i][j] + arr2[i][j]);
    }
    
    return answer;
}