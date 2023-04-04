cnt = 0
keykey = []

def solution(relation):
    answer = 0
    len_c = len(relation[0])
    answer = count(len_c, -1, relation, [() for _ in range(len(relation))], [])
    keykey.sort(key = lambda x:len(x))
    c_key = [keykey[0]]
    for i in range(1, len(keykey)):
        chk = True
        for j in range(len(c_key)):
            x = set(keykey[i]) & set(c_key[j])
            if x == set(keykey[i]) or x == set(c_key[j]):
                chk = False
                break
        if chk:
            c_key.append(keykey[i])
    answer = len(c_key)
    return answer

def count(lc, last_c, relation, keys, key_):
    res = []
    set_key = set()
    answer = 0
    for c in range(last_c + 1, lc):
        for r in range(len(relation)):
            key = tuple(list(keys[r]) + [relation[r][c]])
            res.append(key)
            set_key.add(key)
        key_.append(c)
        if len(res) == len(set_key):
            answer += 1
            keykey.append(key_[:])
        else:
            answer += count(lc, c, relation, res[:], key_[:])
        key_.pop()
        res = []
        set_key = set()
    return answer