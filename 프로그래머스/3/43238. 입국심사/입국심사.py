def solution(n, times):
    left, right = 1, max(times) * n
    
    while left < right:
        mid = (left + right) // 2
        cnt = sum(mid // t for t in times)
        if n <= cnt:
            right = mid
        else:
            left = mid + 1
    
    
    return left