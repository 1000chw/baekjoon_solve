from math import sqrt 
import sys
input = sys.stdin.readline

def dfs(num):
    global tmp_nums
    global visited
    global matched
    if visited[tmp_nums.index(num)]:
        return False
    visited[tmp_nums.index(num)] = 1
    for tmp_num in tmp_nums:
        if primes[tmp_num+num]:
            if tmp_num not in matched or dfs(matched[tmp_num]):
                matched[tmp_num] = num
                return True
    return False
    

n = int(input())
nums = list(map(int, input().split()))
primes = [0]*2001

for i in range(1, 2001):
    if primes[i] == 1:
        continue
    primes[i] = 1
    for j in range(2, int(sqrt(i)+1)):
        if i%j == 0:
            primes[i] = 0
            break

result = []
for num in nums:
    if num == nums[0]:
        continue
    
    matched = {}
    if primes[nums[0] + num]:
        if n == 2:
            result.append(num)
            break
        tmp_nums = [ nums[i] for i in range(1,n) ]
        del tmp_nums[tmp_nums.index(num)]
        for tmp_num in tmp_nums:
            visited = [0]*len(tmp_nums)
            dfs(tmp_num)
            
    if n != 2 and len(matched) == n-2:
        result.append(num)
if not result:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i, end=' ')
