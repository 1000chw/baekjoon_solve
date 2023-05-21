def cutS(s, n):
    res = ''
    num, subs = 1, ''
    while True:
        if len(s) < n:
            if subs:
                if num == 1:
                    res += subs
                else:
                    res += str(num) + subs
            res += s
            break
        tmp, s = s[:n], s[n:]
        if subs == tmp:
            num += 1
        else:
            if num == 1:
                res += subs
            else:
                res += str(num) + subs
            num, subs = 1, tmp
    return len(res)


def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        answer = min(answer, cutS(s, i))
    return answer