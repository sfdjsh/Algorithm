function solution(bandage, health, attacks) {
    var answer = 0;
    
    const last_time = Math.max(...attacks.map((at) => at[0]));   // 몬스터의 마지막 공격 시간   
    let hp = health, heeling_cnt = 0     // 현재 체력, 현재 시전 시간
    
    for (let i = 1; i <= last_time; i++) {
        
        if (hp <= 0) break; // 체력이 0 이하면 종료
        
        var attackInfo = attacks.find(attack => attack[0] === i)
        // 공격 시간이 아닐 때
        if (!attackInfo) {
            heeling_cnt++;
            // 붕대 연속 감기를 성공했을 때, 추가 회복
            if (heeling_cnt === bandage[0]) {
                hp += bandage[2];
                heeling_cnt = 0;
            }
            hp += bandage[1];   // 1초당 회복
        }
        // 공격 당했을 때
        else {
            const damage = attackInfo[1];
            hp -= damage;      
            heeling_cnt = 0;    // 연속 감기 초기화
        }
        
        if (hp > health) hp = health;   // 현재 체력이 최대 체력보다 커지는 것은 불가능
    }
    
    answer = hp <= 0 ? -1 : hp;
    return answer
}