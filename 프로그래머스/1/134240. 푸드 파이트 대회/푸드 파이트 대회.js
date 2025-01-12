function solution(food) {    
    let left_foods = '', right_foods = '';
    
    for (let i = 1; i < food.length; i++) {
        const cnt = parseInt(food[i] / 2);
        left_foods += String(i).repeat(cnt);
        right_foods = String(i).repeat(cnt) + right_foods;
    }
        
    return left_foods + '0' + right_foods;
}