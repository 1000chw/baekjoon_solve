import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
x = max(li)
print(sum(li) - x + x*(len(li)-1))