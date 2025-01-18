import sys

input = sys.stdin.readline

n = int(input())

stairs = []

h = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

for i in range(n):
    stairs.append([h[i], a[i], b[i]])

stairs.reverse()

max_n = [0] * n

def bs(x, k):
    left, right = k+1, n-1

    while left < right:
        mid = (left + right) // 2

        if stairs[mid][0] >= x:
            right = mid
        else:
            left = mid + 1
    return left


for i in range(n-2, -1, -1):
    m = bs(stairs[i][0] + stairs[i][2], i)

    if stairs[m][0] >= stairs[i][0] + stairs[i][2]:
        max_n[i] = max(max_n[m] + stairs[i][1], max_n[i+1])
    else:
        max_n[i] = max_n[i+1]

print(max_n[0])

