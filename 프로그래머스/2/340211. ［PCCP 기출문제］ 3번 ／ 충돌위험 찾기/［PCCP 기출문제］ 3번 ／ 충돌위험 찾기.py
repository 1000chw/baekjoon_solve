from collections import defaultdict
def solution(points, routes):
    answer = 0
    li = defaultdict(set)
    cnt = defaultdict(set)
    
    for route in routes:
        before = 0
        for i in range(len(route)-1):
            x, y = points[route[i]-1]
            nx, ny = points[route[i+1]-1]
            next_ = before + abs(nx-x) + abs(ny-y)+1
            
            for day in range(before, next_):                
                c = len(li[day])
                li[day] |= {(x, y)}
                if (day != before or before == 0) and c == len(li[day]):
                    cnt[(x, y)] |= {day}
                if x < nx:
                    x += 1
                elif x > nx:
                    x -= 1
                else:
                    if y < ny:
                        y += 1
                    else:
                        y -= 1
                if day == next_-1:
                    before = next_-1
    
    for key in cnt.keys():
        answer += len(cnt[key])
    
    return answer