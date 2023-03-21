import sys
input = sys.stdin.readline
for q in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    if x4 < x1 or x2 < x3 or y3 > y2 or y4 < y1:
        print('d')
    elif x4 == x1 or x2 == x3:
        chk = len(set([i for i in range(y3, y4+1)]) & set([i for i in range(y1, y2+1)]))
        if chk > 1:
            print('b')
        else:
            print('c')
    elif y2 == y3 or y1 == y4:
        chk = len(set([i for i in range(x1, x2+1)]) & set([i for i in range(x3, x4+1)]))
        if chk > 1:
            print('b')
        else:
            print('c')
    else:
        print('a')
