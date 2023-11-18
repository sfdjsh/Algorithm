function solution(n) {
    var answer = ''; 
    
    let waterMelon = "수";
    for (let i = 0; i < n; i ++) {
        answer += waterMelon;
        if (waterMelon === "수") {
            waterMelon = "박";
        } else {
            waterMelon = "수";
        }
    }
    
    return answer;
}