def maxn(lst, lst1):
    if max(lst)<0:
        return max(lst)
    x = 0
    for i in lst:
        x += i
        if x < 0:
            lst1.append(x - i)                  
            x = 0
        elif 0 <= x < x - i:
            lst1.append(x - i)
    lst1.append(x)
    return max(lst1)
        
s = input()
n = input().split()
for j in range(len(n)):
    n[j] = int(n[j])
l = []
print(maxn(n, l))



