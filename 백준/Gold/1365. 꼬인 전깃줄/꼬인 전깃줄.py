import sys
from itertools import combinations
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

li = []

for num in nums:
    if not len(li) or li[-1] < num:
        li.append(num)
    else:
        left, right = 0, len(li)-1
        while left < right:
            mid = (left + right)//2
            if li[mid] == num:
                left = mid
                break
            elif num < li[mid]:
                right = mid
            else:
                left = mid + 1
        li[left] = num

print(n - len(li))
