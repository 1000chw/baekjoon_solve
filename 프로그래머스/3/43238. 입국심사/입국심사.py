def solution(n, times):
    answer = max(times) * n
    
    left, right = 1, answer
    
    while left < right:
        mid = (left + right) // 2
        cnt = sum(mid // t for t in times)
        if n <= cnt:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1
    
    cnt = sum(left // t for t in times)
    if n <= cnt:
        answer = min(answer, left)
    
    return answer