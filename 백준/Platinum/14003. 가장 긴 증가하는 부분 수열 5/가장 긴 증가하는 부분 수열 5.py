import sys
input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int, input().split()))
res = [-1000000001]
counts = [0]*(n+1)

for i in range(1, n+1):
    if res[-1] < nums[i]:
        res.append(nums[i])
        counts[i] = len(res)-1
    else:
        left = 0
        right = len(res)

        while left<right:
            mid = (left+right)//2
            if nums[i] > res[mid]:
                left = mid+1
            else:
                right = mid
        res[right] = nums[i]
        counts[i] = right

res1 = len(res)-1
res2 = []
print(res1)
for i in range(n, 0, -1):
    if counts[i] == res1:
        res2.append(nums[i])
        res1 -= 1
        if res1 == 0:
            break

res2 = reversed(res2)
print(*res2)