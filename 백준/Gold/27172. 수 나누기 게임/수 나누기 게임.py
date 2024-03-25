from collections import defaultdict
import sys
n = int(input())
cards = list(map(int, input().split()))
M = max(cards)
cd = {i: [False, 0] for i in range(1, M+1)}
for card in cards:
    cd[card][0] = True
for card in cards:
    for i in range(2, M//card + 1):
        if cd[card * i][0]:
            cd[card * i][1] -= 1
            cd[card][1] += 1
for card in cards:
    print(cd[card][1], end=' ')
