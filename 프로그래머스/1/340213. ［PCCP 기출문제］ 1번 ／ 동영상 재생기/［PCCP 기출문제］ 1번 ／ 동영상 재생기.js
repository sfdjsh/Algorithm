function solution(video_len, pos, op_start, op_end, commands) {
    
    function timeAmount(time) {
        var [minute, second] = time.split(':')
        var amount = Number(minute) * 60 + Number(second)
        return amount
    }
    
    var posAmount = timeAmount(pos);
    var osAmount = timeAmount(op_start);
    var oeAmount = timeAmount(op_end);
    var videoAmount = timeAmount(video_len);
        
    for (command of commands) {
        if (posAmount <= oeAmount && posAmount >= osAmount) posAmount = oeAmount;
        
        if (command === "next") posAmount += 10;
        else posAmount -= 10;
                
        if (posAmount < 0) posAmount = 0;
        else if (posAmount > videoAmount) posAmount = videoAmount;
        
        if (posAmount <= oeAmount && posAmount >= osAmount) posAmount = oeAmount; 
    }
    
    var resultMinute = parseInt(posAmount / 60);
    var resultSecond = posAmount % 60;
    
    return String(resultMinute).padStart(2, "0") + ":" + String(resultSecond).padStart(2, "0");
}