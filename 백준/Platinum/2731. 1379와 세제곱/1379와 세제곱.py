import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

for _ in range(int(input())):
    n = input().rstrip()
    ln = len(n)
    n = int(n)
    answer = 0
    if n % 10 == 1:
        answer = 1
    elif n % 10 == 3:
        answer = 7
    elif n % 10 == 7:
        answer = 3
    else:
        answer = 9
    for i in range(1, ln):
        for j in range(10):
            if pow(pow(10, i)*j+answer, 3, pow(10, i+1)) == n % pow(10, i+1):
                answer += pow(10, i)*j
                break
    print(answer)
