import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M:
    not_workingButtons = input().split()
else:
    not_workingButtons = []

answer = abs(N-100)
for i in range(1000001):
    con_chk = True
    for j in str(i):
        if j in not_workingButtons:
            con_chk = False
            break
    if con_chk:
        answer = min(answer, len(str(i)) + abs(N-i))

print(answer)
