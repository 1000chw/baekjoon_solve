def solution(key, lock):
    answer = False
    padded_lock = [[0]*len(lock) for _ in range(len(key)-1)] + lock + [[0]*len(lock) for _ in range(len(key)-1)]
    for i in range(len(padded_lock)):
        padded_lock[i] = [0]*(len(key)-1) + padded_lock[i] + [0]*(len(key)-1)
        
    keys = [key] + [[[0]*len(key) for _ in range(len(key))] for _ in range(len(key))]
    for k in range(3):
        for i in range(len(key)):
            for j in range(len(key)):
                keys[k+1][j][len(key)-i-1] = keys[k][i][j]
    chkA = False
    for i in range(len(lock)+len(key)-1):
        if chkA: break
        for j in range(len(lock)+len(key)-1):
            if chkA: break
            for key in keys:
                if chkA: break
                for k in range(len(key)):
                    for l in range(len(key)):
                        padded_lock[i+k][j+l] += key[k][l]
                chk = True
                for k in range(len(key) - 1, len(lock)+len(key)-1):
                    if not chk: break
                    for l in range(len(key) - 1, len(lock)+len(key)-1):
                        if padded_lock[k][l] != 1:
                            chk = False
                            break
                if chk:
                    answer = True
                    chkA = True
                    break
                else:
                    for k in range(len(key)):
                        for l in range(len(key)):
                            padded_lock[i + k][j + l] -= key[k][l]
    return answer