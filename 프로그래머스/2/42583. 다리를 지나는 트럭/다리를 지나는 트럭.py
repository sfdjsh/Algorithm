from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    current_bridge_weight = 0
    while truck_weights or bridge:
        time += 1
        
        current_bridge_weight -= bridge.popleft()
        
        if truck_weights:
            if current_bridge_weight + truck_weights[0] <= weight:
                truck_weight = truck_weights.popleft()
                bridge.append(truck_weight)
                current_bridge_weight += truck_weight
                
            else:
                bridge.append(0)
    
    return time