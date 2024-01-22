def solution(cacheSize, cities):
    answer = 0
    
    cache = []
    for c in cities:
        c = c.lower()       # 대소문자 구별 x                                       
        
        if cacheSize:                       # 캐시크기가 있을 때
            if c not in cache:              # cache miss일 때 (도시 이름이 캐시 안에 없을 때) 
                if len(cache) == cacheSize: # 캐시의 크기가 최대라면, 가장 오래된 도시이름 제거
                    cache.pop(0)
                cache.append(c)             
                answer += 5                 # cache miss이므로 +5
            else:                           # cache hit일 때 (도시 이름이 캐시 안에 있을 때)
                cache.remove(c)             # 같은 도시 이름을 제거 
                cache.append(c)            
                answer += 1                 # cache hit이므로 +1
                    
        else:                               # 캐시크기가 없을 때, 저장 불가능
            answer += 5
                
    return answer