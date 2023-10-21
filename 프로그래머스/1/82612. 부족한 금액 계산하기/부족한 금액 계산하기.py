def solution(price, money, count):
    use = 0
    for i in range(1, count + 1):
        use += price * i
    
    if money < use:
        return use - money
    else:
        return 0
    