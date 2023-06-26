import sys
input = sys.stdin.readline

length = 0
left, right = -1000000001, -1000000001
lines = []
for _ in range(int(input())):
    lines.append(list(map(int, input().split())))
lines.sort()
for l, r in lines:
    if l > right:
        length += right-left
        left = l
        right = r
    else:
        right = max(r, right)
length += right-left
print(length)
