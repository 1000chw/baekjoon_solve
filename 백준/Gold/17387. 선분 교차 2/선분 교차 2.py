import sys
input = sys.stdin. readline

def ccw(p1, p2, p3):
    return p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]-p1[1]*p2[0]-p2[1]*p3[0]-p3[1]*p1[0]

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
p1, p2 = sorted([(x1, y1), (x2, y2)])
p3, p4 = sorted([(x3, y3), (x4, y4)])
ccw1, ccw2, ccw3, ccw4 = ccw(p1, p2, p3), ccw(p1, p2, p4), ccw(p3, p4, p1), ccw(p3, p4, p2)
res1, res2 = ccw1*ccw2, ccw3*ccw4

while 1:
    if res1 < 0 and res2 < 0:
        print(1)
        break
    if not res1 or not res2:
        if p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4:
            print(1)
            break
        if not ccw1:
            v1 = [p3[0]-p1[0], p3[1]-p1[1]]
            v2 = [p3[0]-p2[0], p3[1]-p2[1]]
            if v1[0]*v2[0] <= 0 and v1[1]*v2[1] <= 0:
                print(1)
                break
        if not ccw2:
            v1 = [p4[0]-p1[0], p4[1]-p1[1]]
            v2 = [p4[0]-p2[0], p4[1]-p2[1]]
            if v1[0]*v2[0] <= 0 and v1[1]*v2[1] <= 0:
                print(1)
                break
        if not ccw3:
            v1 = [p1[0]-p3[0], p1[1]-p3[1]]
            v2 = [p1[0]-p4[0], p1[1]-p4[1]]
            if v1[0]*v2[0] <= 0 and v1[1]*v2[1] <= 0:
                print(1)
                break
        if not ccw4:
            v1 = [p2[0]-p3[0], p2[1]-p3[1]]
            v2 = [p2[0]-p4[0], p2[1]-p4[1]]
            if v1[0]*v2[0] <= 0 and v1[1]*v2[1] <= 0:
                print(1)
                break
    print(0)
    break
