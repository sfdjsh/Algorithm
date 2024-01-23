def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    cities = [c.lower() for c in cities]
    cache = []
    for city in cities:   
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            answer += 5
    
    return answer