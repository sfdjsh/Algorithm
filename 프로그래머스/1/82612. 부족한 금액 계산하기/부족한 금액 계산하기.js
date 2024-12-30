function solution(price, money, count) {
    var total_price = 0;
    for (let i = 1; i <= count; i++) total_price += price * i
    
    return money < total_price ? total_price - money : 0;
}