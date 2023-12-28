import sys
input = sys.stdin.readline

g = [0]*2001
n = int(input())
g[2] = 1

for i in range(3, n+1):
    gl = []
    for j in range(2, i//2 + 2):
        gl.append(g[j-2]^g[i-j])
    for k in range(2001):
        if k not in gl:
            g[i] = k
            break

print(2 if g[n] == 0 else 1)
