import sys
input = sys.stdin.readline

l, k, c = map(int, input().split())
points = [0] + list(set(map(int, input().split())) | {l})
points.sort()
k = len(points)-1
left, right = 1, l
min_point, length = 0, float('INF')
while left <= right:
    mid = (left + right) // 2
    last = k
    cnt = 0
    m = 0
    M = 0
    chk = False
    for i in range(k-1, 0, -1):
        if points[i+1] - points[i] > mid:
            chk = True
            break
        if points[last] - points[i] > mid:
            if last == i+1:
                cnt += 1
                last = i
            else:
                cnt += 1
                last = i+1
        elif points[last] - points[i] == mid:
            last = i
            cnt += 1
        if cnt == c:
            if points[last] > mid:
                chk = True
            m = points[last]
            break
    if chk:
        left = mid + 1
        continue
    if cnt < c and not chk:
        m = points[1]
        last = 1
        if m > mid:
            left = mid + 1
            continue
    min_point = m
    length = mid
    right = mid - 1
print(length, min_point)
