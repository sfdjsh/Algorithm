function solution(n) {
    const reverse_bin = [...n.toString(3)].reverse().join('');
    
    return parseInt(reverse_bin, 3);
}