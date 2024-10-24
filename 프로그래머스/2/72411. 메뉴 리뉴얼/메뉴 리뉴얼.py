from itertools import combinations

def solution(orders, course):
    
    answer = []
    
    for c in course:
        cos_order = {}
        for order in orders:
            if len(order) >= c:
                com_order = list(combinations(order, c))
                for o in com_order:
                    o = ''.join(sorted(o))
                    if o not in cos_order:
                        cos_order[o] = 1
                    else:
                        cos_order[o] += 1
        
        max_order = []
        for k, v in cos_order.items():
            if v == max(cos_order.values()) and v >= 2:
                max_order.append(k)
                
        answer += max_order
        answer.sort()
    
    return answer