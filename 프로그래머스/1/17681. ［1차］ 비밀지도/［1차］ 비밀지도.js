function solution(n, arr1, arr2) {
    // var answer = [[]];
    var answer = []
    for (let i = 0; i < n; i++) {
        // answer[i] = []
        // var bin_2 = (arr1[i] | arr2[i]).toString(2).padStart(n, 0)
        // for (let j = 0; j < bin_2.length; j++) {
        //     if (bin_2[j] === '1') answer[i].push('#')
        //     else answer[i].push(' ')
        // }
        var bin_2 = (arr1[i] | arr2[i]).toString(2).padStart(n, 0).replace(/1/g,'#').replace(/0/g,' ')
        answer.push(bin_2)
    }
    // answer = answer.map(e => e.join(''))
    return answer;
}