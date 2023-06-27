import sys
from math import sqrt
input = sys.stdin.readline

def gcd(a, b):
    while 1:
        a, b = b, a%b
        if b == 0:
            return a

n = int(input())
A = list(map(int, input().split()))
B = sorted(A)

chk = True
for i in range(n):
    gcd_n = gcd(A[i], B[i])
    a, b = sqrt(A[i]//gcd_n), sqrt(B[i]//gcd_n)
    if a != int(a) or b != int(b):
        chk = False
        break
if chk:
    print('YES')
else:
    print('NO')

