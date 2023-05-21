def chkCorrect(s):
    l, r = 0, 0
    for i in s:
        if i == '(':
            l += 1
        else:
            r += 1
        if r > l:
            return False
    return True

def findUV(s):
    l, r = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            return [s[:i+1], s[i+1:]]

def reverseU(u):
    res = ''
    for i in range(1, len(u)-1):
        if u[i] == '(':
            res += ')'
        else:
            res += '('
    return res

def solution(p):
    answer = ''
    while p != '':
        u, v = findUV(p)
        if chkCorrect(u):
            answer += u
            p = v
        else:
            answer += '(' + solution(v) + ')' + reverseU(u)
            p = ''
    return answer