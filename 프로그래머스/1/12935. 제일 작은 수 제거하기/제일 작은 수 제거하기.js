function solution(arr) {
        
    const minN = Math.min.apply(null, arr);
    arr = arr.filter((num) => {
        return num > minN
    })
    
    return (arr.length === 0) ? [-1] : arr
}