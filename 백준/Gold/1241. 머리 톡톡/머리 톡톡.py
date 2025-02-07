import sys
from collections import defaultdict
from math import sqrt
input = sys.stdin.readline

n = int(input())
d = defaultdict(int)
arr = []
answer = defaultdict(int)

for _ in range(n):
    x = int(input())
    d[x] += 1
    arr.append(x)

keys = list(d.keys())
for key in keys:
    num = int(sqrt(key))
    for i in range(1, num+1):
        if not key % i:
            j = key//i
            if d[i]:
                answer[key] += d[i]
            if i != j and d[j]:
                answer[key] += d[j]

    answer[key] -= 1

for a in arr:
    print(answer[a])
