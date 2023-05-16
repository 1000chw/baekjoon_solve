n = int(input())
a, b = map(int, input().split())
c = int(input())
top = 0
tops = []
for i in range(0, n):
    tops.append(int(input()))
tops.sort(reverse=True)
chk = True
for i in range(0, n):
    if (c+top)//(a+b*i) > (c+top+tops[i])//(a+b*(i+1)):
        chk = False
        print((c+top)//(a+b*i))
        break
    else:
        top += tops[i]

if chk:
    print((c+top)//(a+b*n))
