c = int(input())
for i in range(c):
    scores = list(map(int, input().split()))
    n = scores.pop(0)
    avg = sum(scores)/n
    over_avg = 0
    for j in scores:
        if j > avg:
            over_avg += 1
    print("{:.3f}%".format(round(over_avg/n*100,3)))
    
