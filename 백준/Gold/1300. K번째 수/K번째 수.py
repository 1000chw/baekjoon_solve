n = int(input())
k = int(input())

left = 1
right = k + 0
res = 0
while left <= right:
    cnt = 0
    mid = (left + right)//2
    for i in range(1, n + 1):
        cnt += min(mid//i, n)
    if cnt < k:
        left = mid+1
    else:
        res = mid
        right = mid-1

print(res)