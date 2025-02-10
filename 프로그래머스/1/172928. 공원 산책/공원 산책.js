function solution(park, routes) {    
    const dx = [0, 0, 1, -1], dy = [1, -1, 0, 0] // 동서남북
    const mx = park.length, my = park[0].length
    
    let x = 0, y = 0
    for (let i = 0; i < mx; i++) {
        for (let j = 0; j < my; j++) {
            if (park[i][j] === "S") x = i, y = j;
        }
    }
    
    routes.map(route => {
        let [arrow, cnt] = route.split(" ");
        cnt = Number(cnt);
        
        let tmp_x = x, tmp_y = y;
        for (let i = 0; i < cnt; i++) {
            if (arrow === "E") {
                x = x + dx[0], y = y + dy[0];
                if (x < 0 || x >= mx || y < 0 || y >= my || park[x][y] === "X") {
                    x = tmp_x, y = tmp_y;
                    break;
                }  
            }
            else if (arrow === "W") {
                x = x + dx[1], y = y + dy[1];
                if (x < 0 || x >= mx || y < 0 || y >= my || park[x][y] === "X") {
                    x = tmp_x, y = tmp_y;
                    break;
                } 
            }
            else if (arrow === "S") {
                x = x + dx[2], y = y + dy[2];
                if (x < 0 || x >= mx || y < 0 || y >= my || park[x][y] === "X") {
                    x = tmp_x, y = tmp_y;
                    break;
                }   
            }
            else if (arrow === "N") {
                x = x + dx[3], y = y + dy[3];
                if (x < 0 || x >= mx || y < 0 || y >= my || park[x][y] === "X") {
                    x = tmp_x, y = tmp_y;
                    break;
                }   
            }
        }
    })
    
    return [x, y];
}