function solution(bandage, health, attacks) {
    var answer = 0;
    
    var last_time = Math.max(...attacks.map((at) => at[0]))
    var hp = health
    var hp_cnt = 0
    
    for (let i = 1; i <= last_time; i++) {
        
        if (hp <= 0) break;
        
        var attackInfo = attacks.find(attack => attack[0] === i)
        if (!attackInfo) {
            hp_cnt++;
            if (hp_cnt === bandage[0]) {
                hp += bandage[2];
                hp_cnt = 0;
            }
            hp += bandage[1];
        } else {
            let damage = attackInfo[1];
            hp -= damage;
            hp_cnt = 0;
        }
        
        if (hp > health) {
            hp = health;
        }
        
    }
    
    answer = hp <= 0 ? -1 : hp;
    return answer
}