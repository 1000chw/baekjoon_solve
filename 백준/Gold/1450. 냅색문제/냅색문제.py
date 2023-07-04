import sys
from itertools import combinations
input = sys.stdin.readline

N, C = map(int, input().split())

arr = list(map(int, input().split()))
A, B = arr[:N//2], arr[N//2:]
comb_A, comb_B = [], []

for i in range(N//2+1):
    comb_A.extend(list(map(sum, combinations(A, i))))
for i in range(N-N//2+1):
    comb_B.extend(list(map(sum, combinations(B, i))))
comb_A.sort()

res = 0
for b in comb_B:
    if b > C:
        continue
    start, end, mid = 0, len(comb_A)-1, len(comb_A)//2
    while start <= end:
        if b + comb_A[mid] > C:
            end = mid - 1
        else:
            start = mid+1
        mid = (start + end) // 2
    res += end+1
print(res)
