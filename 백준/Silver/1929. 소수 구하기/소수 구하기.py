import math
n = input()
x = n.split()
Number = 0


def isprime(n1):
    if n1 == 1:
        return False
    for i in range(2, int(math.sqrt(n1))+1):
        if n1 % int(i) == 0:
            return False
    return True


lst = []
for i in range(int(x[0]), int(x[1])+1):
    if isprime(int(i)):
        print(i)

