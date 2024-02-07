import sys
input = sys.stdin.readline
k = 2100001
N = [True]*k
PN = []
for i in range(2, k):
    if N[i]:
        PN.append(i)
        for j in range(2, (k-1)//i+1):
            N[i*j] = False

for i in range(int(input())):
    n = sum(map(int, input().split()))
    if n % 2 == 0:
        if n == 2:
            print("NO")
        else:
            print("YES")
    else:
        n -= 2
        if n == 1:
            print("NO")
            continue
        chk = True
        for pn in PN:
            if pn == n:
                break
            if n % pn == 0:
                chk = False
                break
        if chk:
            print("YES")
        else:
            print("NO")
