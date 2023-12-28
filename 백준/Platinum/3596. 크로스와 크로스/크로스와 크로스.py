import sys
input = sys.stdin.readline

g = [0]*2001
n = int(input())

for i in range(1, n+1):
    gl = []
    for j in range(i // 2 + 1):
        left = max(0, j - 2)
        right = i - 1 - min(i - 1, j + 2)
        gl.append(g[left] ^ g[right])
    gl.sort()
    for k in range(2001):
        if k not in gl:
            g[i] = k
            break

print(2 if g[n] == 0 else 1)
