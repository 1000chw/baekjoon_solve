def solution(name):
    answer = 0
    mid = 'M'
    chk, cnt = False, 0
    first = 0
    total_count = 0
    min_move = len(name) - 1
    for i in range(len(name)):
        n = name[i]
        if n == 'A':
            if not chk:
                chk = True
                cnt = 1
                first = i
            else:
                cnt += 1
        else:
            if chk:
                chk = False
                if first == 0:
                    min_move = min(min_move, len(name) - first - cnt)
                else:
                    min_move = min(min_move, first-2 + len(name) - cnt, first - 1 + (len(name) - first - cnt) * 2)
            if n <= mid:
                total_count += ord(n) - ord('A')
            else:
                total_count += ord('Z') - ord(n) + 1
    if chk:
        min_move = min(min_move, first-1 if first else 0)
    answer = total_count + min_move
        
    return answer