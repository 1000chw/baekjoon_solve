N, M, K = map(int, input().split())

end = 1
count = N

if N < M + K - 1 or N > M*K:
    print(-1)
else:
    while True:
        M -= 1
        count -= K
        if M == 0:
            for i in range(N, end-1, -1):
                print(i, end=' ')
            break
        if count <= 0 or count // M == 0:
            for i in range(end+K+count-M-1, end-1, -1):
                print(i, end=' ')
            for i in range(end+K+count-M, N+1):
                print(i, end=' ')
            break
        else:
            for i in range(end+K-1, end-1, -1):
                print(i,end=' ')
            end += K
