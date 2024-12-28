def solution(s):
    cnt_l = 0
    
    for x in s:
        if x == '(':
            cnt_l += 1
        else:
            if not cnt_l:
                return False
            else:
                cnt_l -= 1
    if cnt_l:
        return False
    return True