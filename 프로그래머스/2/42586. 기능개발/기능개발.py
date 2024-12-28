from math import ceil

def solution(progresses, speeds):
    answer = []
    
    days = []
    
    for i in range(len(progresses)):
        days.append(ceil((100-progresses[i])/speeds[i]))
    
    day = days[0]
    cnt = 1
    for i in range(1, len(days)):
        if day >= days[i]:
            cnt += 1
        else:
            answer.append(cnt)
            day = days[i]
            cnt = 1
    answer.append(cnt)
    return answer