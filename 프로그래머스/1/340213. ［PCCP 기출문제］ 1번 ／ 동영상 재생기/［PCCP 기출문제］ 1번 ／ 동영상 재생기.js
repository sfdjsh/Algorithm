function solution(video_len, pos, op_start, op_end, commands) {
    
    // 초 단위로 바꿔주는 함수
    function timeAmount(time) {
        const [minute, second] = time.split(':');
        const amount = Number(minute) * 60 + Number(second);
        return amount;
    }
    
    let posAmount = timeAmount(pos);            // 재생위치 시간
    const osAmount = timeAmount(op_start);        // 오프닝 시작 시간
    const oeAmount = timeAmount(op_end);          // 오프닝 끝나는 시간
    const videoAmount = timeAmount(video_len);    // 동영상의 시간
        
    for (command of commands) {
        // 재생 위치가 오프닝 시작과 끝나는 시간 안에 있으면, 오프닝 끝나는 시간으로 이동
        if (posAmount <= oeAmount && posAmount >= osAmount) posAmount = oeAmount;
        
        if (command === "next") posAmount += 10;    // 10초 후로 이동
        else posAmount -= 10;                       // 10초 전으로 이동
                
        if (posAmount < 0) posAmount = 0;   // 영상의 처음 위치(0분 0초)
        else if (posAmount > videoAmount) posAmount = videoAmount;  // 영상의 마지막 위치(동영상 시간)
        
        // 이동 후, 재생 위치가 오프닝 시작과 끝나는 시간 안에 있으면, 오프닝 끝나는 시간으로 이동
        if (posAmount <= oeAmount && posAmount >= osAmount) posAmount = oeAmount; 
    }
    
    const resultMinute = parseInt(posAmount / 60);
    const resultSecond = posAmount % 60;
    
    return String(resultMinute).padStart(2, "0") + ":" + String(resultSecond).padStart(2, "0");
}