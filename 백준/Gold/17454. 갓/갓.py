import sys
input = sys.stdin.readline


def solve():
    dh, ds, hd, hs, sd, sh = map(int, input().split())
    if hd > hs or sd > sh or (hd == hs and sd == sh):
        print('GOD')
        return
    cx = [hd * sd, dh * sd, (sh-sd) * sd]
    if cx[2]:
        cy = [sd * (sh-sd), ds * (sh-sd), (hs-hd) * (sh-sd)]
        if cx[0] == cy[2]:
            print('KDH')
            return 0
        calcx = int((cx[1] + cy[1]) / (cx[0] - cy[2]) + 1)
        if calcx <= 0:
            print('KDH')
            return
        else:
            print('GOD')
            return
    else:
        print('GOD')
        return



for _ in range(int(input())):
    solve()