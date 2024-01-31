import sys
input = sys.stdin.readline
INF = float('inf')

def solve(s):
    joy = 0
    ls = len(s)
    for i in range(ls):
        joy += min(ord(s[i])-ord('A'), ord('Z')-ord(s[i])+1)
    if 'A' not in s:
        joy += ls-1
        return joy
    else:
        isA = s[0] == 'A'
        left = 0
        notA = []
        for i in range(ls):
            if not isA:
                if s[i] == 'A':
                    notA.append((left, i-1))
                    isA = True
            else:
                if s[i] != 'A':
                    isA = False
                    left = i
        if s[-1] != 'A':
            notA.append((left, ls-1))
        notA.append((ls, 0))
        return chk_min_move(notA, ls) + joy

def chk_min_move(notA, ls):
    res = ls-notA[0][0]
    for i in range(len(notA)-1):
        res = min(res, notA[i][1]*2+ls-notA[i+1][0], (ls-notA[i+1][0])*2+notA[i][1])
    return res


for _ in range(int(input())):
    print(solve(input().strip()))
