def solution(lottos, win_nums):
    
    lotto = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}   # 맞힌 수 : 등 수
      
    max_rank = 0    # 최고 순위
    min_rank = 0    # 최저 순위
    
    for w in win_nums:
        if w in lottos:
            max_rank += 1
            min_rank += 1
    
    max_rank += lottos.count(0)     # 알아볼 수 없는 번호(0) 최고 순위에 더하기
    
    return [lotto[max_rank], lotto[min_rank]]