function solution(video_len, pos, op_start, op_end, commands) {
    var answer = '';
    
    function timeAmount(time) {
        var [hour, minute] = time.split(':')
        var amount = Number(hour) * 60 + Number(minute)
        return amount
    }
    
    var pos_amount = timeAmount(pos)
    var os_amount = timeAmount(op_start)
    var oe_amount = timeAmount(op_end)
    var video_amount = timeAmount(video_len)
        
    for (command of commands) {
        
        if (pos_amount < oe_amount && pos_amount > os_amount) pos_amount = oe_amount
        
        if (command === "next") {
            pos_amount += 10
        } else if (command === "prev") {
            pos_amount -= 10
        }
                
        if (pos_amount < 0) {
            pos_amount = 0
        } else if (pos_amount > video_amount) {
            pos_amount = video_amount
        }
        
        if (pos_amount <= oe_amount && pos_amount >= os_amount) pos_amount = oe_amount
        
    }
    
    var result_hour = parseInt(pos_amount / 60)
    var result_minute = pos_amount % 60
    
    return String(result_hour).padStart(2, "0") + ":" + String(result_minute).padStart(2, "0");
}