import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().split())
xs, ys = [], []
dx, dy = 0, 0
for _ in range(n):
    x, y = map(int, input().split())
    dx += abs(x)
    dy += abs(y)
    xs.append(x)
    ys.append(y)

xs.sort()
ys.sort()

x, y = 0, 0
for command in input().rstrip():
    if command == 'S':
        y += 1
        py = bisect.bisect_left(ys, y)
        dy += py * 2 - n
        print(dx + dy)
    elif command == 'J':
        y -= 1
        py = bisect.bisect_right(ys, y)
        dy += n - 2 * py
        print(dx + dy)
    elif command == 'I':
        x += 1
        px = bisect.bisect_left(xs, x)
        dx += px * 2 - n
        print(dx + dy)
    else:
        x -= 1
        px = bisect.bisect_right(xs, x)
        dx += n - 2 * px
        print(dx + dy)

