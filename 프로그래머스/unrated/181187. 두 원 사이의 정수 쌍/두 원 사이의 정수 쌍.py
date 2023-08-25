def solution(r1, r2):
    quar = 0
    
    for i in range(0, r1):
        quar += int((r2**2 - i**2) ** 0.5) - int((r1**2 - i**2 - 1) ** 0.5)
        
    for i in range(r1, r2):
        quar += int((r2**2 - i**2) ** 0.5)
        
    return quar * 4