function solution(wallpaper) {
    let lux = 50, luy = 50
    let rdx = 0, rdy = 0
    
    for (let i = 0; i < wallpaper.length; i++) {
        for (let j = 0; j < wallpaper[0].length; j++) {
            if (wallpaper[i][j] === '#') {
                lux = Math.min(lux, i)
                luy = Math.min(luy, j)
                rdx = Math.max(rdx, i + 1)
                rdy = Math.max(rdy, j + 1)
            }
        }
    }    
    return [lux, luy, rdx, rdy];
}