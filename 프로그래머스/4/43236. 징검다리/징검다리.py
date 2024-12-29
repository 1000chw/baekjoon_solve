def solution(distance, rocks, n):
    answer = 0
    left, right = 1, distance
    new_rocks = [0] + list(sorted(rocks)) + [distance]
    max_d = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        before = 0
        for now in range(1, len(new_rocks)):
            if new_rocks[now] - new_rocks[before] >= mid:
                before = now
            else:
                cnt += 1
        if cnt > n:
            right = mid - 1
        else:
            max_d = max(max_d, mid)
            left = mid + 1
            
    return max_d