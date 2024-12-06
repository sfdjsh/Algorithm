function solution(N, stages) {
    var answer = [];
    
    for (let i = 1; i < N + 1; i++) {        
        let fail = stages.filter(e => e === i).length / stages.length
        answer.push([i, fail])
        stages = stages.filter(e => e !== i)
    }
        
    return [...answer.sort((a, b) => b[1] - a[1]).map(stage => stage[0])];
}