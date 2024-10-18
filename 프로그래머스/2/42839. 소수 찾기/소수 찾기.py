from math import sqrt
from itertools import permutations

def solution(numbers):
    answer = 0
    number_list = list(numbers)
    isPrime = makePrimes()
    a = set()
    for i in range(1, len(number_list)+1):
        a |= set(map(int, map("".join, permutations(number_list, i))))
    number_set = list(a)
    for number in number_set:
        if isPrime[number]:
            answer += 1
    return answer

def makePrimes():
    l = 10000000
    isPrime = [True]*(l+1)
    isPrime[0] = False
    isPrime[1] = False
    
    for i in range(2, int(sqrt(l))+1):
        if isPrime[i]:
            for j in range(2, l//i+1):
                isPrime[i * j] = False
    return isPrime

def findPrimeNumber(number_list, used_list, isPrime, cnt, n, number):
    if cnt == n:
        number = int(number)
        if isPrime[number]:
            isPrime[number] = False
            return 1
        return 0
    count = 0
    for i in range(len(number_list)):
        if not used_list[i]:
            used_list[i] = True
            count += findPrimeNumber(number_list, used_list, isPrime, cnt+1, n, number+number_list[i])
            used_list[i] = False
            
    return count
    