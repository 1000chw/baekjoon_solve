import sys
input = sys.stdin. readline

c_s = {}
balls = []
sums = {}
cnt = {}
res = {}
N = int(input())
for i in range(N):
    color, size = map(int, input().split())
    balls.append((size, color, i))
    sums[color] = 0

balls.sort()
last_size = 0
size_sum = 0
same_sum = 0
last_color = 0
last_color_same = 0
for ball in balls:
    if ball[0] > last_size:
        size_sum += same_sum + last_color_same
        last_color_same = 0
        same_sum = 0
        res[ball[2]] = size_sum - sums[ball[1]]
        size_sum += ball[0]
        sums[ball[1]] += ball[0]
        last_color = ball[1]
        last_size = ball[0]
    elif last_color != ball[1]:
        same_sum += ball[0] + last_color_same
        sums[ball[1]] += ball[0]
        res[ball[2]] = size_sum - sums[ball[1]]
        last_color_same = 0
        last_color = ball[1]
    else:
        res[ball[2]] = size_sum + last_color_same - sums[ball[1]]
        sums[ball[1]] += ball[0]
        last_color_same += ball[0]

for i in range(len(res)):
    print(res[i])
