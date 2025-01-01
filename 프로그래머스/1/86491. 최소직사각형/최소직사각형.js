function solution(sizes) {
    let max_w = 0, max_h = 0;
    
    for (let size of sizes) {
        sort_size = size.sort((a, b) => a - b);
        max_w = Math.max(max_w, sort_size[0]);
        max_h = Math.max(max_h, sort_size[1]);
    }
        
    return max_w * max_h;
}