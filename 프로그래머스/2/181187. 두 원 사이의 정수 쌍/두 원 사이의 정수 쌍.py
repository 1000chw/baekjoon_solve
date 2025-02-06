from math import sqrt, ceil, floor
def solution(r1, r2):
    answer = 0
    r1s, r2s = r1**2, r2**2
    
    for i in range(1, r2+1):
        if i < r1:
            y1 = ceil(sqrt(r1s - i**2))
            y2 = floor(sqrt(r2s - i**2))
            answer += y2 - y1 + 1
        else:
            y2 = floor(sqrt(r2s - i**2))
            answer += y2 + 1  
    
    return answer*4