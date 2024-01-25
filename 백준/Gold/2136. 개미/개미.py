import sys
input = sys.stdin.readline

n, l = map(int, input().split())

minus, plus = 0, 0
ants = []
minuss, pluss = [], []
for i in range(1, n+1):
    ant = int(input())
    if ant < 0:
        minus += 1
        minuss.append(-ant)
        ants.append((-ant, i))
    else:
        plus += 1
        pluss.append(l - ant)
        ants.append((ant, i))
ants.sort()
minuss.sort()
pluss.sort()

if minus == 0:
    print(ants[0][1], pluss[-1])
elif plus == 0:
    print(ants[-1][1], minuss[-1])
else:
    if minuss[-1] > pluss[-1]:
        print(ants[minus-1][-1], minuss[-1])
    else:
        print(ants[minus][-1], pluss[-1])
