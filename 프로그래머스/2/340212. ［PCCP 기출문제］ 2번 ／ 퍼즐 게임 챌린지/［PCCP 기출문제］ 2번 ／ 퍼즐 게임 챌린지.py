def solution(diffs, times, limit):
    answer = 0
    lt = len(times)
    left, right = 1, max(diffs)
    while left <= right:
        mid = (left+right)//2
        l = 0
        for i in range(lt):
            if diffs[i] > mid:
                l += (diffs[i]-mid)*(times[i-1] + times[i]) + times[i]
            else:
                l += times[i]
        
        if l <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer