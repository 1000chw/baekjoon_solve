from math import sqrt
def solution(n, k):
    answer = 0
    k_num = ""
    while n != 0:
        k_num = str(n%k)+k_num
        n //= k
    num = ""
    for n in k_num:
        if n == "0":
            if num != "":
                answer += chkPrime(int(num))
            num = ""
        else:
            num += n
    if num != "":
        answer += chkPrime(int(num))
    return answer

def chkPrime(num):
    if num == 1:
        return 0
    max_n = int(sqrt(num))+1
    chk = True
    for i in range(2, max_n):
        if not num%i:
            return 0
    return 1
    