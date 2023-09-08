def solution(wallpaper):
    
    lux, luy = 50, 50
    rdx, rdy = 0, 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if lux > i:
                    lux = i
                if luy > j:
                    luy = j
                if rdx < i + 1:
                    rdx = i + 1
                if rdy < j + 1:
                    rdy = j + 1
        
    return [lux, luy, rdx, rdy]