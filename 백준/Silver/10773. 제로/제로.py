import sys
input = sys.stdin.readline

k = int(input())
lis = []
for _ in range(k):
    x = int(input())
    if x == 0:
        lis.pop()
    else:
        lis.append(x)
print(sum(lis))
