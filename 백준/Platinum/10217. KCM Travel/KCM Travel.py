import sys
 
T=int(input())
INF=sys.maxsize
 
for _ in range(T):
    N,M,K=map(int,sys.stdin.readline().split())
    ticket=[[] for _ in range(N+1)]
    for _ in range(K):
        u,v,c,d=map(int,sys.stdin.readline().split())
        ticket[u].append([v,c,d])
 
 
    DP=[[INF for _ in range(M+1)] for _ in range(N+1)]
    DP[1][0]=0
 
    for c in range(M+1):
        for d in range(1,N+1):
            if DP[d][c]==INF:continue
            t=DP[d][c]
            for dv,dc,dd in ticket[d]:
                if dc+c>M:
                    continue
                DP[dv][dc+c]=min(DP[dv][dc+c],t+dd)
 
    result=min(DP[N])
 
    if result==INF:
        print('Poor KCM')
    else:
        print(result)
