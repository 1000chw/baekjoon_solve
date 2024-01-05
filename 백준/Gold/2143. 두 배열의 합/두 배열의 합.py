import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_dict = defaultdict(int)
b_dict = defaultdict(int)

for i in range(n):
    s_a = 0
    for j in range(i, n):
        s_a += a[j]
        a_dict[s_a] += 1

for i in range(m):
    s_b = 0
    for j in range(i, m):
        s_b += b[j]
        b_dict[s_b] += 1

answer = 0

a_key = a_dict.keys()
b_key = list(sorted(b_dict.keys()))

for i in a_key:
    target = t - i
    start, end = 0, len(b_key) - 1
    found = False
    while start < end:
        mid = (start + end) // 2
        if b_key[mid] == target:
            answer += b_dict[b_key[mid]] * a_dict[i]
            found = True
            break
        elif b_key[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    if not found and b_key[start] == target:
        answer += b_dict[b_key[start]] * a_dict[i]
print(answer)
