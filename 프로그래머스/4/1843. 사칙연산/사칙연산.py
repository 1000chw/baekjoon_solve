def solution(arr):
    answer = -1
    int_arr = []
    acc_arr = []

    for i in range(len(arr)):
        if i % 2:
            acc_arr.append(arr[i])
        else:
            int_arr.append(int(arr[i]))
    INF = 300000
    mdp = [[INF] * (len(arr) // 2 + 1) for _ in range(len(arr) // 2 + 1)]
    Mdp = [[-INF] * (len(arr) // 2 + 1) for _ in range(len(arr) // 2 + 1)]

    def solve(l, r):
        if l == r:
            mdp[l][r] = int_arr[l]
            Mdp[l][r] = int_arr[r]
            return mdp[l][r], Mdp[l][r]

        if mdp[l][r] != INF and Mdp[l][r] != -INF:
            return mdp[l][r], Mdp[l][r]

        minN, maxN = INF, -INF

        for i in range(l, r):
            l_m, l_M = solve(l, i)
            r_m, r_M = solve(i + 1, r)
            if acc_arr[i] == "-":
                minN = min(minN, l_m - r_M)
                maxN = max(maxN, l_M - r_m)
            else:
                minN = min(minN, l_m + r_m)
                maxN = max(maxN, l_M + r_M)
        mdp[l][r] = minN
        Mdp[l][r] = maxN

        return mdp[l][r], Mdp[l][r]

    minN, maxN = solve(0, len(int_arr) - 1)

    return maxN