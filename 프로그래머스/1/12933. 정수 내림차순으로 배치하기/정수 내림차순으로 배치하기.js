function solution(n) {    
    n = String(n);
    const lst_n = [ ...n ];
    lst_n.sort().reverse();    
    
    return Number(lst_n.join(''));
}