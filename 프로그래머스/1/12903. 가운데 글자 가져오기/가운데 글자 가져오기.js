function solution(s) {
    const idx = parseInt(s.length / 2);
    
    return s.length % 2 ? s[idx] : s[idx - 1] + s[idx];
}