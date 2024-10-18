def solution(numbers):
    answer = 0
    number_list = list(numbers)
    used_list = [False] * len(number_list)
    isPrime = makePrimes()
    for i in range(1, len(number_list)+1):
        answer += findPrimeNumber(number_list, used_list, isPrime, 0, i, '')
    
    return answer

def makePrimes():
    l = 10000000
    isPrime = [True]*(l+1)
    isPrime[0] = False
    isPrime[1] = False
    
    for i in range(2, l):
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
    