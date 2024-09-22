import sys
input = sys.stdin.readline


def BallChange():
    n, m = map(int, input().split())
    balls = [str(i) for i in range(1, n + 1)]
    for i in range(m):
        x, y = map(lambda x: int(x) - 1, input().split())
        balls[x], balls[y] = balls[y], balls[x]
    return ' '.join(balls)


print(BallChange())
