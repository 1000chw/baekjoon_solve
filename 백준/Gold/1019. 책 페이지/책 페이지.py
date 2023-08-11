import sys
input = sys.stdin.readline

n = int(input())
result = [0]*10
ten = 1
while n != 0:
    while n%10 != 9:
        for i in str(n):
            result[int(i)] += ten
        n -= 1
    if n < 10:
        for i in range(n+1):
            result[i] += ten
        result[0] -= ten
        break
    else:
        for i in range(10):
            result[i] += (n//10+1)*ten
        result[0] -= ten
        n //= 10
        ten *= 10
for i in result:
    print(i, end=' ')
