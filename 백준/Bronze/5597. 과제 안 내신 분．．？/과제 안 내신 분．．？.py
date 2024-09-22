import sys
input = sys.stdin.readline


def solve():
    students = [False] * 30
    for _ in range(28):
        students[int(input()) - 1] = True

    for i in range(30):
        if not students[i]:
            print(i + 1)


solve()
