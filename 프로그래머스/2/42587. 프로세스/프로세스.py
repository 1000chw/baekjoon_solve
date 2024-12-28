from collections import deque
def solution(priorities, location):
    answer = 0
    
    q = deque()
    
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    priorities.sort(reverse=True)
    idx = 0
    cnt = 0
    while True:
        if q[0][0] == priorities[idx]:
            cnt += 1
            if q[0][1] == location:
                answer = cnt
                break
            q.popleft()
            idx += 1
        else:
            q.append(q.popleft())
    
    return answer