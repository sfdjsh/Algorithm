function solution(n, lost, reserve) {    
    // var lst = [...lost]
    
    lost.sort((a, b) => a - b)
    reserve.sort((a, b) => a - b)
    
    lost.map((num) => {
        if (reserve.includes(num)) {
            reserve = reserve.filter(e => e != num)
            lost = lost.filter(e => e != num)
        } else if (reserve.includes(num - 1) && !lost.includes(num - 1)) {
            reserve = reserve.filter(e => e != num - 1)
            lost = lost.filter(e => e != num)  
        } else if (reserve.includes(num + 1) && !lost.includes(num + 1)) {
            reserve = reserve.filter(e => e != num + 1)
            lost = lost.filter(e => e != num)
        }
    })
    
    return n - lost.length;
}