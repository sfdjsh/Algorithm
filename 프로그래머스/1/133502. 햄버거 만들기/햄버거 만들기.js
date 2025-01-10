function solution(ingredient) {
    var answer = 0;
    const bugger_order = [1, 2, 3, 1];
    
    let idx = 0
    while (idx <= ingredient.length - 4) {
        if (ingredient[idx] !== 1) idx++;
        else {
            const order = ingredient.slice(idx, idx + 4);
            const order_filter = order.filter((ele, i) => ele !== bugger_order[i]).length;
            if (!order_filter) {
                ingredient.splice(idx, 4);
                answer++;
                idx = idx < 4 ? 0 : idx - 2
            } else idx++;  
        }
    }
    
    return answer;
}