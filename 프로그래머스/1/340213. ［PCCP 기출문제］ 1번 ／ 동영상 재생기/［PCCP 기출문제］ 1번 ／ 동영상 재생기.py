def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    vl = int(video_len[0:2]) * 60 + int(video_len[3:])
    p = int(pos[0:2]) * 60 + int(pos[3:])
    os = int(op_start[0:2]) * 60 + int(op_start[3:])
    oe = int(op_end[0:2]) * 60 + int(op_end[3:])
    for c in commands:
        if os <= p <= oe:
            p = oe
        if c == 'next':
            p = min(vl, p + 10)
        else:
            p = max(0, p - 10)
    if os <= p <= oe:
        p = oe
    answer = f'{p//60:02}:{p%60:02}'
    return answer