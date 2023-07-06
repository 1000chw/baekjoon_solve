import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, 0
sumN = arr[0]
res = 100001
while 1:
    if res == 1 or r == N-1 and sumN < S:
        break
    if sumN >= S:
        res = min(res, r - l + 1)
        sumN -= arr[l]
        l += 1
    elif sumN <= 0:
        r = l
        sumN = arr[l]
    else:
        r += 1
        sumN += arr[r]
if res == 100001:
    print(0)
else:
    print(res)