function solution(schedules, timelogs, startday) {
    var answer = 0;
    
    function admitWork(time) {
        let hour = Math.floor(time / 100);
        let minute = time % 100 + 10;
        if (minute >= 60) {
            hour += 1;
            minute -= 60;
        }
        return hour * 100 + minute
    }
    
    for (let i = 0; i < timelogs.length; i++) {
        let tmp = 1;
        const schedule = admitWork(schedules[i]);
        
        let day = startday - 1;
        for (let j = 0; j < timelogs[i].length; j++) {
            if (day !== 5 && day !== 6) {
                if (timelogs[i][j] > schedule) {
                    tmp = 0;
                    break;
                }
            }
            
            day = (day + 1) % 7;
        }
        
        answer += tmp;
    }
    
    return answer;
}