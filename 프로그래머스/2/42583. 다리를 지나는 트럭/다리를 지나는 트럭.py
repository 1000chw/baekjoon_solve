from collections import deque
def solution(bridge_length, weight, truck_weights):
    days = 0
    now_weight = 0
    cnt = len(truck_weights)
    q = deque()
    idx = 0
    while cnt:
        days += 1
        if not q:
            q.append((truck_weights[0], days))
            now_weight += truck_weights[0]
            idx += 1
        else:
            if days-q[0][1] == bridge_length:
                now_weight -= q[0][0]
                q.popleft()
                cnt -= 1
            if idx < len(truck_weights) and now_weight + truck_weights[idx] <= weight:
                now_weight += truck_weights[idx]
                q.append((truck_weights[idx], days))
                idx += 1
    return days